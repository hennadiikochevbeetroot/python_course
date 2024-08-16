from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class FileSystemElementType(Enum):
    FILE = 'FILE'
    DIRECTORY = 'DIRECTORY'


@dataclass(kw_only=True)
class Metadata:
    creation_time: datetime
    last_modification_time: datetime
    byte_size: int

    def __str__(self):
        return (
            f'creation_time = {self.creation_time}\n'
            f'last_modification_time = {self.last_modification_time}\n'
            f'byte_size = {self.byte_size}\n'
        )


class FileSystemElement:
    def __init__(self, name: str, is_directory: bool):
        self.name = name
        self.is_directory = is_directory
        self.creation_time = datetime.now()
        self.last_modification_time = self.creation_time

    def update_last_modification_time(self):
        self.last_modification_time = datetime.now()


class File(FileSystemElement):
    def __init__(self, name: str, content: str):
        super().__init__(name, False)
        self.content = content
        self.byte_size = len(content)

    def update_content(self, content: str) -> None:
        self.content = content
        self.update_last_modification_time()


class Directory(FileSystemElement):
    def __init__(self, name: str):
        super().__init__(name, True)
        self.byte_size = 4096
        self.content: dict[str, Directory | File] = {}

    def add_file(self, name: str, content: str) -> None:
        file = File(name, content)
        self.content[name] = file
        self.update_last_modification_time()

    def add_directory(self, name: str) -> None:
        directory = Directory(name)
        self.content[name] = directory
        self.update_last_modification_time()

    def get_element(self, name) -> File | Directory:
        return self.content.get(name)

    def get_contents(self) -> list[File | Directory]:
        return list(self.content.values())

    def get_file_content(self, name):
        file = self.content.get(name)
        if isinstance(file, File):
            return file.content

        raise TypeError('Not A File')

    def find_files_by_name(self, name: str) -> list[str]:
        result_files = []
        for element in self.content.values():
            if isinstance(element, File) and name in element.name:
                result_files.append(element.name)
            elif isinstance(element, Directory):
                directory_found_files = element.find_files_by_name(name)
                if directory_found_files:
                    result_files.extend(directory_found_files)

        return result_files


    def list_elements(self) -> list[tuple[str, str]]:
        directory_elements = []
        for name, element in self.content.items():
            element_type = FileSystemElementType.DIRECTORY.value if isinstance(
                element,
                Directory
                ) else FileSystemElementType.FILE.value
            directory_elements.append((element_type, name))

        return directory_elements

    def delete_element(self, name: str):
        self.content.pop(name, None)
        self.update_last_modification_time()


class SimpleFileSystem:
    def __init__(self):
        self.root_directory = Directory('/')

    def create_file(self, path: str, content: str) -> None:
        names = path.split('/')
        directory_names, file_name = names[:-1], names[-1]
        current_directory = self.root_directory
        for directory_name in directory_names:
            current_directory.add_directory(directory_name)
            current_directory = current_directory.get_element(directory_name)

        current_directory.add_file(file_name, content)

    def read_file(self, path: str) -> str:
        names = path.split('/')
        directory_names, file_name = names[:-1], names[-1]
        current_directory = self.root_directory
        for directory_name in directory_names:
            current_directory = current_directory.get_element(directory_name)

        return current_directory.get_file_content(file_name)

    def update_file(self, path: str, content: str) -> None:
        names = path.split('/')
        directory_names, file_name = names[:-1], names[-1]
        current_directory = self.root_directory
        for directory_name in directory_names:
            current_directory = current_directory.get_element(directory_name)

        file = current_directory.get_element(file_name)
        file.update_content(content)

    def delete_file(self, path: str) -> None:
        names = path.split('/')
        directory_names, file_name = names[:-1], names[-1]
        current_directory = self.root_directory
        for directory_name in directory_names:
            current_directory = current_directory.get_element(directory_name)

        current_directory.delete_element(file_name)

    def get_file_metadata(self, path: str) -> Metadata:
        names = path.split('/')
        directory_names, file_name = names[:-1], names[-1]
        current_directory = self.root_directory
        for directory_name in directory_names:
            current_directory = current_directory.get_element(directory_name)

        file = current_directory.get_element(file_name)

        return Metadata(
            creation_time=file.creation_time,
            last_modification_time=file.last_modification_time,
            byte_size=file.byte_size,
        )

    def list_elements(self) -> list[tuple[str, str]]:
        return self.root_directory.list_elements()

    def find_files_by_name(self, name: str) -> list[str]:
        result_files = []

        current_directory = self.root_directory
        for element in current_directory.get_contents():
            if isinstance(element, File) and name in element.name:
                result_files.append(element.name)
            elif isinstance(element, Directory):
                result_files.extend(element.find_files_by_name(name))

        return result_files







# Example usage:
fs = SimpleFileSystem()
fs.create_file("one/example.txt", "Hello, World!")
print(fs.read_file("one/example.txt"))  # Output: Hello, World!

fs.create_file("example2.txt", "222Hello, World!")

fs.update_file("one/example.txt", "Updated content.")
print(fs.read_file("one/example.txt"))  # Output: Updated content.

print(fs.list_elements())


print(fs.list_elements())

# print(fs.get_file_metadata("one/example.txt"))

print(fs.find_files_by_name('ex'))




# fs.create_file("new_file.txt", "This is a new file.")
# print(fs.list_files())  # Output: ['example.txt', 'new_file.txt']
#
# fs.delete_file("example.txt")
#   # Output: ['new_file.txt']

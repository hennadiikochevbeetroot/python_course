# Implement a circular music playlist
# Enhance DLL to be circular (last node next element is going to be root element)
# Song as a Node, Playlist is a circular DLL
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Song:
    author: str
    title: str
    prev: Song | None = None
    next: Song | None = None

    def __str__(self):
        return f'Song: {self.title} by {self.author}'


class Playlist:
    def __init__(self):
        self.first_song: Song | None = None

    def append(self, author: str, title: str):
        if self.first_song is None:
            self.first_song = Song(author, title)
            self.first_song.prev = self.first_song
            self.first_song.next = self.first_song
        else:
            current_song = self.first_song
            while current_song.next is not self.first_song:
                current_song = current_song.next

            current_song.next = Song(author, title, prev=current_song, next=self.first_song)
            self.first_song.prev = current_song.next

    def play_songs_num(self, num: int):
        current_song = self.first_song
        for _ in range(num):
            print(current_song)
            current_song = current_song.next


if __name__ == '__main__':
    playlist = Playlist()
    playlist.append('Weeknd', 'Blinding Lights')
    playlist.append('Ed Sheeran', 'Shape of You')
    playlist.append('Luis Fonsi', 'Despacito')

    playlist.play_songs_num(5)

# Implement Commit as Node and Git as SLL
from __future__ import annotations
import uuid


class Commit:
    def __init__(self, hash: str, author: str, message: str, parent: Commit | None = None):
        self.hash = hash
        self.author = author
        self.message = message
        self.parent = parent

    def __str__(self):
        return f'{self.hash[:8]} by {self.author}: {self.message}'


class Git:
    def __init__(self, user: str = 'default user'):
        self.user = user
        self.latest_commit: Commit | None = None

    def set_user(self, username: str):
        self.user = username

    def commit(self, message: str):
        self.latest_commit = Commit(
            hash=uuid.uuid4().hex,
            author=self.user,
            message=message,
            parent=self.latest_commit,
        )

    def log(self):
        current_commit = self.latest_commit
        while current_commit is not None:
            print(current_commit)
            current_commit = current_commit.parent


if __name__ == '__main__':
    git = Git()
    git.commit('init commit')
    git.commit('second commit')
    git.set_user('New user')
    git.commit('commit from new user')

    git.log()

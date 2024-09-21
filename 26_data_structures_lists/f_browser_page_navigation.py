# Implement Browser with page back and page forward functionality based on DLL:
# Page is a Node, Browser utilizes DLL of Pages
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Page:
    url: str
    prev: Page | None = None
    next: Page | None = None

    def __str__(self):
        return f'Page URL: {self.url}'


class Browser:
    def __init__(self):
        self.current_page: Page | None = None

    def go_to_url(self, url: str):
        if self.current_page is None:
            self.current_page = Page(url)
        else:
            self.current_page.next = Page(url, prev=self.current_page)
            self.current_page = self.current_page.next

    def go_back(self):
        if self.current_page is None or self.current_page.prev is None:
            return
        self.current_page = self.current_page.prev

    def go_forward(self):
        if self.current_page is None or self.current_page.next is None:
            return
        self.current_page = self.current_page.next

    def __str__(self):
        return f'Current page: {self.current_page}'


if __name__ == '__main__':
    browser = Browser()
    browser.go_to_url('google.com')
    browser.go_to_url('beetrootacademy.com')
    browser.go_to_url('lms.beetrootacademy.com')

    print(browser)
    browser.go_back()
    print(browser)
    browser.go_back()
    print(browser)
    browser.go_forward()
    print(browser)

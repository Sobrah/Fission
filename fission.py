import re
import os
import requests
import project

from conditions import conditions
from urllib.parse import urlparse, urljoin


class Trigger:
    def __init__(self, url: str) -> None:
        BASE_PARTS = urlparse(url)
        GLOBALS = globals()

        if not (BASE_PARTS.scheme and BASE_PARTS.netloc):
            raise ValueError("Invalid URL.")
        if not "STORED_URLS" in GLOBALS:
            global STORED_URLS
            STORED_URLS = set()
        if not "BASE_DOMAIN" in GLOBALS:
            global BASE_DOMAIN
            BASE_DOMAIN = BASE_PARTS.netloc

        Fission(url)


class Fission:
    def __init__(self, url: str) -> None:
        print(project.paint("Requesting:", "green", "italic"), url)
        response = requests.get(url)
        self.base_url = response.url
        self.location, self.directory = self.address(response.url)[:2]
        self.content = response.text
        STORED_URLS.add(response.url)

        if response.headers["Content-type"].split("/")[0] == "text":
            self.collective()
        elif conditions(response.headers):
            self.content = response.content
            self.save(mode="wb")
            

    def collective(self) -> str:
        if urls := self.find_urls(self.content):
            for tag, attribute, url in urls:
                valid_url = urljoin(self.base_url, url)
                if urlparse(valid_url).netloc == BASE_DOMAIN:
                    if not valid_url in STORED_URLS:
                        Fission(valid_url)

                    vu_address = self.address(valid_url)
                    relative_path = os.path.relpath(vu_address[1], start=self.directory)

                    self.content = self.content.replace(
                        tag, f'{attribute}="{relative_path}/{vu_address[2]}"'
                    )

        return self.save()

    @classmethod
    def find_urls(cls, text: str) -> set:
        urls = set(
            re.findall(
                r"((href|src)=(?:\"|\')([^<>=\'\";?#]+)(?:[^<>=\'\"]*)(?:\'|\"))",
                text,
                re.IGNORECASE,
            )
        )
        # Tag, Attribute, Quotation, URL
        return urls

    @classmethod
    def address(cls, url) -> tuple:
        netloc, path = urlparse(url)[1:3]
        file_name = "index.html"

        if matches := re.search(r"^(/(?:.+/)*)([^\./]+\.[^\./]+)$", path):
            path, file_name = matches.groups()
        if not path.endswith("/"):
            path += "/"

        directory = (netloc + path).replace(".", "_")

        return (directory + file_name), directory, file_name

    def save(self, mode="w") -> str:
        print(project.paint("Saving:", "blue", "italic"), self.location)
        os.makedirs(self.directory, exist_ok=True)
        with open(self.location, mode) as file:
            file.write(self.content)

        return self.location


if __name__ == "__main__":
    Trigger(input("URL: "))

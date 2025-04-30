import re
from typing import Dict, Optional

import zipfile
from fastapi import UploadFile
from xml.etree import ElementTree


class EBook:
    def __init__(self):
        self.order: list[str] = []
        self.parts: Dict[str, str] = {}
        self.content: str = ""

    @classmethod
    def from_upload_file(cls, upload_file: UploadFile) -> Optional["EBook"]:
        """
        Generates in-memory EBook from upload file
        """

        try:
            with zipfile.ZipFile(upload_file.file, "r") as zf:
                ebook = EBook._extract_and_consolidate(zf)
                return ebook
        except KeyError:
            return None

    @classmethod
    def _extract_and_consolidate(cls, zip_file: zipfile.ZipFile) -> "EBook":
        """
        Extract files from zip_file
        """
        ebook = EBook()

        for file in zip_file.namelist():
            if file.endswith(".opf"):
                with zip_file.open(file) as opf_file:
                    tree = ElementTree.parse(opf_file)

                manifest_items = tree.findall(".//{http://www.idpf.org/2007/opf}item")

                # Extend search to include .htm files
                files_order = [
                    item.attrib["href"]
                    for item in manifest_items
                    if "html" in item.attrib["href"]
                    or item.attrib["href"].endswith(".htm")
                ]

                ebook.order = files_order

            if (
                file.endswith(".xhtml")
                or file.endswith(".html")
                or file.endswith(".htm")
            ):
                with zip_file.open(file) as content_file:
                    content = content_file.read()

                ebook.parts[file] = content.decode("utf-8")

        ebook._consolidate()
        return ebook

    def _consolidate(self) -> str:
        """
        Parses parts to human readable str
        """

        self.content = ""

        for file_name in self.order:
            part_content = self.parts[file_name]
            print(part_content)
            # html_content = re.findall("<.*?>", part_content)
            cleaned_content = self._remove_html_tags_and_empty_lines(part_content)

            self.content += f"\n\nChapter: {file_name}\n\n{cleaned_content}\n"

    def _remove_html_tags_and_empty_lines(self, text: str):
        # Remove all spaces and tabs first
        text = re.sub(
            r"\s+", " ", text
        )  # This collapses all whitespace into single spaces for cleaner processing

        # Insert a newline before the start and after the end of <p> and <h1> tags
        text = re.sub(r"<div[^>]*>", "", text)
        text = re.sub(r"</div>", "\n", text)
        text = re.sub(r"<p[^>]*>", "", text)
        text = re.sub(r"</p>", "\n", text)
        text = re.sub(r"<h1[^>]*>", "", text)
        text = re.sub(r"</h1>", "\n", text)
        text = re.sub(r"<a[^>]*>", "", text)
        text = re.sub(r"</a>", "\n", text)
        text = re.sub(r"<span[^>]*>", "", text)
        text = re.sub(r"<link[^>]*/>", "", text)
        text = re.sub(r"</span>", "\n", text)
        # Remove DOCTYPE declarations
        text = re.sub(r"<!DOCTYPE[^>]*>", "", text)
        text = re.sub(r"&nbsp;", " ", text)
        # Remove CSS style blocks
        text = re.sub(r"<style.*?>.*?</style>", "", text, flags=re.DOTALL)

        # Remove HTML comments
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

        # Remove all other HTML tags
        text = re.sub(r"<.*?>", "", text)

        # Remove consecutive spaces and tabs
        # text = re.sub(r"\s+", " ", text)

        # Split text into lines and remove empty lines
        lines = text.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]

        return "\n".join(non_empty_lines)

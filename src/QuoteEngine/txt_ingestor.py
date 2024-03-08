"""Text Ingestor module for parsing quotes from TXT files."""

from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """A class for ingesting quotes from TXT files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is .txt.

        :param path: The path to the file.
        :return: True if the file extension is .txt, False otherwise.
        """
        return path.endswith(".txt")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from a TXT file.

        :param path: The path to the TXT file.
        :return: A list of QuoteModel objects.
        """
        quotes = []
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" - ")
                    if len(parts) == 2:
                        body, author = parts
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        return quotes

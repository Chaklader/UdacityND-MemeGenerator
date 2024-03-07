from typing import List

import docx

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    A class for ingesting quotes from DOCX files.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is .docx.

        :param path: The path to the file.
        :return: True if the file extension is .docx, False otherwise.
        """
        return path.endswith(".docx")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from a DOCX file.

        :param path: The path to the DOCX file.
        :return: A list of QuoteModel objects.
        """
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                parts = paragraph.text.split(" - ")
                if len(parts) == 2:
                    body, author = parts
                    quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(quote)
        return quotes
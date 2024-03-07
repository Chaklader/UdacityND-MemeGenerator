import subprocess
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """
    A class for ingesting quotes from PDF files.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is .pdf.

        :param path: The path to the file.
        :return: True if the file extension is .pdf, False otherwise.
        """
        return path.endswith(".pdf")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from a PDF file.

        :param path: The path to the PDF file.
        :return: A list of QuoteModel objects.
        """
        quotes = []
        text = subprocess.check_output(["pdftotext", "-layout", path, "-"], universal_newlines=True)
        for line in text.splitlines():
            line = line.strip()
            if line:
                parts = line.split(" - ")
                if len(parts) == 2:
                    body, author = parts
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
        return quotes

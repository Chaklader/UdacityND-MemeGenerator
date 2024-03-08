"""Ingestor module for ingesting quotes from various file types."""

from typing import List

from .csv_ingestor import CSVIngestor
from .docx_Ingestor import DocxIngestor
from .ingestor_interface import IngestorInterface
from .pdf_ingestor import PDFIngestor
from .quote_model import QuoteModel
from .txt_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """A class for ingesting quotes from various file types."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from a file.

        :param path: The path to the file.
        :return: A list of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise ValueError(f"Unsupported file type: {path}")

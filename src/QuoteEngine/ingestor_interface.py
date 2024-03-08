"""Ingestor Interface module defining an abstract base class for ingestors."""

from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class for ingestors."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the ingestor can handle the given file type.

        :param path: The path to the file.
        :return: True if the ingestor can handle the file type, False otherwise.
        """
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from the given file.

        :param path: The path to the file.
        :return: A list of QuoteModel objects.
        """
        pass
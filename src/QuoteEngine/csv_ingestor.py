from typing import List

import pandas as pd

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    A class for ingesting quotes from CSV files.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is .csv.

        :param path: The path to the file.
        :return: True if the file extension is .csv, False otherwise.
        """
        return path.endswith(".csv")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes from a CSV file using pandas.

        :param path: The path to the CSV file.
        :return: A list of QuoteModel objects.
        """
        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
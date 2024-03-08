"""Quote Model module defining the QuoteModel class."""


class QuoteModel:
    """A class representing a quote."""

    def __init__(self, body, author):
        """
        Initialize a QuoteModel object.

        :param body: The body of the quote.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

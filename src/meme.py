"""Meme module for generating memes."""

import argparse
import os
import random

from MemeEngine.meme_engine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote_model import QuoteModel
from utils import get_tmp_path


def generate_meme(path=None, body=None, author=None):
    """Generate a meme by a given path and quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    tmp_folder_path = get_tmp_path()

    meme = MemeEngine(tmp_folder_path)

    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate meme.')
    parser.add_argument(
        '--path', type=str, help='path to an image file'
    )
    parser.add_argument(
        '--body', type=str, help='quote body to add to the image'
    )
    parser.add_argument(
        '--author', type=str, help='quote author to add to the image'
    )
    args = parser.parse_args()

    path = generate_meme(args.path, args.body, args.author)
    print(path)

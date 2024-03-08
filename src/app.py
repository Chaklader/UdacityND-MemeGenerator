"""Flask app module for serving the meme generator web interface."""

import random
import os
import requests

from flask import Flask, render_template, abort, request, send_from_directory

from QuoteEngine.ingestor import Ingestor
from MemeEngine.meme_engine import MemeEngine
from utils import get_tmp_path

app = Flask(__name__)


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_quote_paths = [os.path.join(base_dir, path)
                            for path in quote_files
                            ]

    quotes = []
    for f in absolute_quote_paths:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    absolute_images_path = os.path.join(base_dir, images_path)

    imgs = []
    for root, dirs, files in os.walk(absolute_images_path):
        imgs.extend([os.path.join(root, name) for name in files])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    tmp_folder_path = get_tmp_path()
    meme = MemeEngine(tmp_folder_path)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/tmp/<path:filename>')
def serve_meme(filename):
    """Serve meme from directory."""
    return send_from_directory(get_tmp_path(), filename)


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    tmp_folder_path = get_tmp_path()

    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    response = requests.get(img_url, allow_redirects=True)
    tmp = os.path.join(tmp_folder_path, 'tmp.jpg')
    open(tmp, 'wb').write(response.content)

    meme = MemeEngine(tmp_folder_path)
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

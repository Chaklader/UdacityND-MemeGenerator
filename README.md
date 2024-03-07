# Meme Generator

The Meme Generator is a Python project that allows you to generate memes by combining images with quotes. It provides a command-line interface for generating memes and a web interface for creating memes interactively.

## Project Overview

The Meme Generator consists of two main modules:

### QuoteEngine:
This module is responsible for ingesting various types of files that contain quotes. It includes classes for parsing quotes from different file formats such as CSV, Docx, PDF, and Text files. The quotes are encapsulated in a QuoteModel class.

### MemeEngine:
This module is responsible for generating memes by manipulating images. It includes a MemeEngine class that takes an image, resizes it to a specified width while maintaining the aspect ratio, adds a quote to the image, and saves the generated meme.

## Setup and Installation

To set up and run the Meme Generator project, follow these steps:


Create a virtual environment (optional but recommended):

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```shell
pip3 install -r requirements.txt
```

Run the Meme Generator:

To generate a meme using the command-line interface:

```shell
python -m src.meme --path "path/to/image.jpg" --body "Quote body" --author "Quote author"
```

To start the web interface:

```shell
python -m src.app
Open a web browser and navigate to http://localhost:5000 to access the web interface.
```

<h3>Sub-Modules</h3>

QuoteEngine

    The QuoteEngine module consists of the following sub-modules:
    
    QuoteModelDefines the QuoteModel class that represents a quote with a body and an author.
    
    IngestorInterface: Defines an abstract base class for quote ingestors. It includes abstract methods for checking if a file can be ingested and parsing quotes from a file.
    CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor: Implement the IngestorInterface for parsing quotes from CSV, Docx, PDF, and Text files, respectively.
    Ingestor: Provides a facade class for ingesting quotes from different file types. It encapsulates the logic for selecting the appropriate ingestor based on the file extension.

MemeEngine

    The MemeEngine module consists of the following sub-module:
    
    MemeEngine: Defines the MemeEngine class responsible for generating memes. It includes methods for loading an image, resizing it, adding a quote to the image, and saving the generated meme.
    Examples
    Here are a few examples of how to use the Meme Generator:

Generate a meme using the command-line interface:

```shell
python -m src.meme --path "path/to/image.jpg" --body "I have a dream" --author "Martin Luther King Jr."
```

Generate a random meme using the web interface:

Start the web server:

```shell
python -m src.app
```

Open a web browser and navigate to http://localhost:5000.
Click the "Random" button to generate a random meme. Create a custom meme using the web interface:

Start the web server:

```shell
python -m src.app
```

Open a web browser and navigate to http://localhost:5000/create.

Fill in the form with the image URL, quote body, and quote author.
Click the "Create Meme" button to generate the custom meme.
Feel free to explore and enjoy generating memes with the Meme Generator!

**License**

This project is licensed under the MIT License. See the LICENSE file for more information.


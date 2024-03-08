<h2>Meme Generator</h2>
<br>
The Meme Generator is a Python project that allows you to generate memes by combining images with quotes. It provides a command-line interface for generating memes and a web interface for creating memes interactively.

<h3>Project Overview</h3>
The Meme Generator consists of two main modules:

<h4>QuoteEngine:</h4> 

This module is responsible for ingesting various types of files that contain quotes. It includes classes for parsing quotes from different file formats such as CSV, Docx, PDF, and Text files. The quotes are encapsulated in a QuoteModel class.
MemeEngine: This module is responsible for generating memes by manipulating images. It includes a MemeEngine class that takes an image, resizes it to a specified width while maintaining the aspect ratio, adds a quote to the image, and saves the generated meme.
Setup and Installation
To set up and run the Meme Generator project, follow these steps:

- Clone the project repository and Navigate to the project directory:

```shell
git clone git@github.com:Chaklader/UdacityND-MemeGenerator.git

cd UdacityND-MemeGenerator
```

- Create a virtual environment (optional but recommended) and install project dependencies:

```shell
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
```

<h3>Project Structure: Sub-Modules</h3>


1. QuoteEngine: Defines the QuoteModel class that represents a quote with a body and an author.
IngestorInterface: Defines an abstract base class for quote ingestors. It includes abstract methods for checking if a file can be ingested and parsing quotes from a file.
CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor: Implement the IngestorInterface for parsing quotes from CSV, Docx, PDF, and Text files, respectively.
Ingestor: Provides a facade class for ingesting quotes from different file types. It encapsulates the logic for selecting the appropriate ingestor based on the file extension.

2. MemeEngine: Defines the MemeEngine class responsible for generating memes. It includes methods for loading an image, resizing it, adding a quote to the image, and saving the generated meme.
Examples
Here are a few examples of how to use the Meme Generator:

Run the Meme Generator
Generate a meme using the CLI
Enter inside the /src directory.

Install the required libraries:

shell


brew install freetype fontconfig poppler
Generate the meme from the terminal:

shell


python3 meme.py
Generate a meme using the web interface
The web server can be started from the CLI or IDE. It is recommended to use the IDE for a better development experience.

Start the web server:

python3 app.py
Open a web browser and navigate to http://localhost:5000.

Click the "Random" button to generate a random meme.

Create a custom meme using the web interface
Start the web server:


python3 app.py
Open a web browser and navigate to http://localhost:5000/create.

Fill in the form with the image URL, quote body, and quote author.

Click the "Create Meme" button to generate the custom meme.

Feel free to explore and enjoy generating memes with the Meme Generator!

License
This project is licensed under the MIT License. See the LICENSE file for more information.


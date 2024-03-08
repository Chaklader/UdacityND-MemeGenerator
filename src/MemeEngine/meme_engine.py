"""Meme Engine module for generating memes."""

import textwrap
from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """A class representing a meme."""

    def __init__(self, output_dir):
        """
        Initialize a MemeEngine object with the given output directory.

        :param output_dir: The directory where the generated memes saved.
        """
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generate a meme by loading an image and saving the modified image.

        :param img_path: The path to the input image.
        :param text: The body of the quote to be added to the image.
        :param author: The author of the quote.
        :param width: The desired width of the output image (default: 500px).
        :return: The path to the generated meme image.
        """
        try:
            if img_path is None or not os.path.exists(img_path):
                raise ValueError("Invalid image path")

            print(f"Output directory: {self.output_dir}")

            img = Image.open(img_path)

            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.ANTIALIAS)

            draw = ImageDraw.Draw(img)

            # Set initial font size
            font_size = 30

            # Wrap the text
            wrapped_text = textwrap.fill(text, width=30)
            wrapped_text += f"\n- {author}"

            # Dynamically adjust the font size based on text length
            while True:
                font = ImageFont.truetype(lilita_one_font_path(),
                                          size=font_size)
                text_width, text_height = draw.textsize(wrapped_text,
                                                        font=font)

                if text_width <= width - 40 and text_height <= height - 40:
                    break

                font_size -= 2

            # Calculate the position to draw the wrapped text
            text_position = ((width - text_width) // 2,
                             (height - text_height) // 2)

            # Draw the wrapped text on the image
            draw.text(text_position, wrapped_text, font=font, fill='white')

            output_path = os.path.join(self.output_dir,
                                       f"meme_{random.randint(0, 100000)}.jpg")
            img.save(output_path)

            return output_path

        except Exception as e:
            print(f"Error generating meme: {str(e)}")


def lilita_one_font_path() -> str:
    """
    Get the path to the Lilita One font file.

    :return: The path to the Lilita One font file.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_dir, "_data/fonts/LilitaOne-Regular.ttf")

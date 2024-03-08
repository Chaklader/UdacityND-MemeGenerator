from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    def __init__(self, output_dir):
        """
        Initializes a MemeEngine object with the given output directory.

        :param output_dir: The directory where the generated memes will be saved.
        """
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generates a meme by loading an image, resizing it, adding text, and saving the modified image.

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
            font = ImageFont.truetype(lilita_one_font_path(), size=20)
            text_position = (random.randint(30, width - 200), random.randint(30, height - 50))
            draw.text(text_position, f'"{text}"\n- {author}', font=font, fill='white')

            output_path = os.path.join(self.output_dir, f"meme_{random.randint(0, 100000)}.jpg")
            img.save(output_path)

            return output_path

        except Exception as e:
            print(f"Error generating meme: {str(e)}")


def lilita_one_font_path() -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_dir, "_data/fonts/LilitaOne-Regular.ttf")

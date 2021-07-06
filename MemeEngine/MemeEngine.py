"""Create a library to generate memes."""

from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """Create a meme & save it in the output folder."""

    def __init__(self, out_path: str):
        """Initialize meme object with user-defined \
        output path to save the meme."""
        self.out_path = out_path

    def make_meme(self, img_path: str, msg_body=None, msg_author=None) -> str:
        """Resize the input image to a max width of 500 pixels \
        while maintaining the aspect ratio. Draw message \
        quote & author onto the meme.

        :param img_path = Path which contains the meme image
        :param msg_body = Message quote to be written on the image
        :param msg_author = Message's author to be written on the image
        """
        width = 500
        with Image.open(img_path) as img:

            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

            if msg_body is not None and msg_author is not None:
                complete_msg = f'{msg_body}\n- {msg_author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('calibri.ttf', size=30)
                txt = draw.text((10, 20), complete_msg, font=font, fill='red')

            final_out_path = self.out_path +\
                f'/{random.randint(0,10000)}_out.jpg'
            img.save(final_out_path)
            return final_out_path

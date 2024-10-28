import time
from blinkable import Blinkable
from smiley import Smiley


class Sick(Smiley, Blinkable):
    """
   Provides a Smiley with a happy expression
    """

    def __init__(self):
        super().__init__(complexion=self.GREEN)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
       Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [42, 43, 44, 45, 51, 52]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [10, 17, 18, 13, 22, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
        Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()

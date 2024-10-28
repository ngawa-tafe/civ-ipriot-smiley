"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
from sad import Sad
from angry import Angry
from sick import Sick

def main():

    happy = Happy()
    happy.show()
    time.sleep(1)
    happy.blink()
'''
    saddy = Sad()
    saddy.show()
    time.sleep(1)
    saddy.blink(0.5)
    time.sleep(1)
    saddy.blink(0.5)

    angry = Angry()
    angry.show()
    time.sleep(1)
    angry.blink(1)
    time.sleep(1)

    sick = Sick()
    sick.show()
    time.sleep(1)
    sick.blink()
    time.sleep(1)
'''

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()


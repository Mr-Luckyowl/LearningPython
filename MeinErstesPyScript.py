#
# -*- coding: iso-8859-1 -*-
# Kommentar iso-8859-1 mit Umlaute!
 
import os
import sys

print ('Das Script wird ausgeführt ohne Fehler? - oder etwa nicht ?')

from math import radians
import numpy as np # type: ignore # installed with matplotlib
import matplotlib.pyplot as plt # type: ignore

# def main():
#     x = np.arange(0, radians(1800), radians(12))
#     plt.plot(x, np.cos(x), 'b')
#     plt.show()

def main():
# - - - - - - - - - - - - 
    for x in range(0, 1800, 12):
        print(x)

main()






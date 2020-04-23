#!/bin/python3

import math
import os
import random
import re
import sys


def solve():

	s = "Jadson Marliere de Oliveira #capitalize"

    for el in s[:].split():
        s = s.replace(el, el.capitalize())

    return s


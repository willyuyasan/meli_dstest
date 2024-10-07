import sys
import os

DIR = os.getcwd()
sys.path.append(DIR)

DIR = os.path.dirname(__file__)
sys.path.append(DIR)

DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR)
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from csv import reader
import numpy as np

def read_datafile(file_name):
    '''
    the skiprows keyword is for heading
    but I don't know if trailing lines
    can be specifies
    '''
    data = 
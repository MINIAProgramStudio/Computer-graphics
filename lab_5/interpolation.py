import ImageContainer as IC
import numpy as np

def neighbor(input_IC, desired_size, ds_is_width = True):
    output_IC = IC.ImageContainer()
    IC.ImageContainer =
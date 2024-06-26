import numpy
import cv2
import copy



class ImageContainer:
    def __init__(self, path=None):
        if path != None:  # if path is defined, import the image
            self.path = path
            self.data = cv2.imread(path)

    path = None
    data = []

    def show(self):  # show the image and wait for anykey
        cv2.imshow(self.path, self.data)
        cv2.waitKey(0)

    def save(self):
        cv2.imwrite(self.path, self.data)


def IC_to_monochrome(input_IC, red=0.36, green=0.53, blue=0.11):  # create monochromatic copy of an image
    if type(input_IC.data[0][0]) != list or not isinstance(input_IC, ImageContainer):
        Exception("IC_to_monochrome accepts only rgb image containers")
    output_IC = copy.deepcopy(input_IC)  # create copy of an image
    output_IC.path = None  # delete a path of a copy

    pos_y = 0
    for row in output_IC.data:
        pos_x = 0
        for pixel in row:
            output_IC.data[pos_y][pos_x] = int(
                pixel[0] * red + pixel[1] * green + pixel[2] * blue)  # monochromatic transformation
            pos_x += 1
        pos_y += 1

    return output_IC  # return a monochromatic copy


def monochrome_to_binary(input_IC):
    if type(input_IC.data[0][0]) != int or not isinstance(input_IC, ImageContainer):
        Exception("monochrome_to_binary accepts only monochromatic image containers")
    output_IC = copy.deepcopy(input_IC)  # create copy of an image
    output_IC.path = None  # delete a path of a copy

    if True:
        brightness_graph = [0] * 256
        for row in input_IC.data:
            for pixel in row:
                brightness_graph[pixel[0]] += 1

        total_brightness = sum(brightness_graph)

        brightness_possibility = [0] * 256
        for i in range(0, 255):
            brightness_possibility[i] = brightness_graph[i] / total_brightness

        def q1(t):
            output = sum(brightness_possibility[0:t])
            if output != 0:
                return output
            else:
                return 0.0001

        def q2(t):
            output = sum(brightness_possibility[t + 1:])
            if output != 0:
                return output
            else:
                return 0.0001

        def mu1(t):
            output = 0
            for i in range(0, t):
                output += i * brightness_possibility[i] / q1(t)
            return output

        def mu2(t):
            output = 0
            for i in range(t + 1, 255):
                output += i * brightness_possibility[i] / q2(t)
            return output

        def main_disp(t):
            return q1(t) * q2(t) * ((mu1(t) * mu2(t)) ** 2)

        max_val = -10 ** 10
        t_max = 0
        for t in range(0, 255):
            value = main_disp(t)
            if value > max_val:
                t_max = t
                max_val = value
        pos_y = 0
        for row in output_IC.data:
            pos_x = 0
            for pixel in row:
                if pixel[0] > t_max:
                    output_IC.data[pos_y][pos_x] = 255
                else:
                    output_IC.data[pos_y][pos_x] = 0
                pos_x += 1
            pos_y += 1

        return output_IC


def monochrome_binary_slice(input_IC, channel=2, bit=1):
    output_IC = copy.deepcopy(input_IC)
    pos_y = 0
    for row in input_IC.data:
        pos_x = 0
        for pixel in row:
            value = int((pixel[channel] % (2 ** bit)) / (2 ** (bit - 1)))
            if value != 0:
                output_IC.data[pos_y][pos_x] = 255
            else:
                output_IC.data[pos_y][pos_x] = 0
            pos_x += 1
        pos_y += 1
    return output_IC


def built_in_image(input_IC, binary_IC, channel=2, bit=1):
    output_IC = copy.deepcopy(input_IC)
    binary_height = len(binary_IC.data)
    binary_width = len(binary_IC.data[0])
    pos_y = 0
    for row in input_IC.data:
        pos_x = 0
        for pixel in row:
            value = pixel[channel]
            unbited_value = value - int((value % (2 ** bit)) / (2 ** (bit - 1)))
            bitted_value = unbited_value + int(binary_IC.data[pos_y % binary_height][pos_x % binary_width][0] / 255) * (
                        2 ** (bit - 1))
            output_IC.data[pos_y][pos_x][channel] = bitted_value

            pos_x += 1
        pos_y += 1
    return output_IC


def built_in_text(input_IC, binary_text, channel=2, bit=1):
    output_IC = copy.deepcopy(input_IC)
    binary_length = len(binary_text)
    pos_y = 0
    width = len(input_IC.data[0])
    for row in input_IC.data:
        pos_x = 0
        for pixel in row:
            if (pos_y * width + pos_x) < binary_length:
                value = pixel[channel]
                unbited_value = value - int((value % (2 ** bit)) / (2 ** (bit - 1)))
                bit_to_be_bitted = int(binary_text[(pos_y * width + pos_x) % binary_length])
                bitted_value = unbited_value + bit_to_be_bitted * (2 ** (bit - 1))
                output_IC.data[pos_y][pos_x][channel] = bitted_value
            else:
                value = pixel[channel]
                unbited_value = value - int((value % (2 ** bit)) / (2 ** (bit - 1)))
                output_IC.data[pos_y][pos_x][channel] = unbited_value
            pos_x += 1
        pos_y += 1
    return output_IC

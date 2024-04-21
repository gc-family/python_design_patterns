import pprint
from functools import *
from itertools import *
from collections import *
from PIL import Image

path = r"..\Python_regular_expretion\simple_image.png"
imageObj = Image.open(path)
print(imageObj.size)


class TiledStrategy:
    def __call__(self, image_file, desktop_size):
        in_img = Image.open(image_file)
        out_img = Image.new("RGB", desktop_size)
        num_tiles = [o // i + 1 for o, i in zip(out_img.size, in_img.size)]
        print(num_tiles)
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x + 1),
                        in_img.size[1] * (y + 1)
                    )
                )
        return out_img


class CenteredStrategy:
    def __call__(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(
            in_img,
            (
                left,
                top,
                left + in_img.size[0],
                top + in_img.size[1]
            )
        )
        return out_img


class ScaledStrategy:
    def __call__(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = in_img.resize(desktop_size)
        return out_img


if __name__ == '__main__':
    result = CenteredStrategy()
    result2 = result(path, (500, 500))
    with open('result.png', mode="wb") as file:
        file.write(result2.tobytes())
        print("successfully the file is resized")

"""Resample partner logos to a consistent size, currently 300x300.

The grid of partner institutions on the main index page looks best when we can
guarantee that all of the images are in the partner grid are the same size.

Run this script before committing images and using them in the build.


"""
import math
import sys

from PIL import Image
from PIL import ImageOps

TARGET_WIDTH_PIXELS = 300
TARGET_HEIGHT_PIXELS = 150


def adjust(source_image_path, target_image_path,
           target_image_size=(TARGET_WIDTH_PIXELS, TARGET_HEIGHT_PIXELS)):
    print(f"Adjusting {source_image_path} --> {target_image_path}")
    print(f"Using target image size {target_image_size}")
    with Image.open(source_image_path) as im:
        # Scale the image so that it's smaller than the target width and height
        source_width, source_height = im.size
        scale_factor_height = target_image_size[1] / source_height
        scale_factor_width = target_image_size[0] / source_width
        scaled_image = ImageOps.scale(im, min(scale_factor_height,
                                              scale_factor_width))

    # Expand borders with transparency until we get an image of the target
    # dimensions.
    scaled_width, scaled_height = scaled_image.size
    bordered = ImageOps.expand(
        scaled_image,
        border=(int((target_image_size[0]-scaled_width)/2),
                int((target_image_size[1]-scaled_height)/2)),
        fill=(0, 0, 0, 0))
    bordered.save(target_image_path)

    print("Complete")


if __name__ == '__main__':
    adjust(sys.argv[1], sys.argv[2])

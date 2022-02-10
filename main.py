#!/usr/bin/python3

import os
# from os import path
from PIL import Image
# import glob
from pathlib import Path

folder_path = 'src'

# image_files = [folder_path + '/' + f for f in glob.glob('**/*.PNG')]


def png_to_jpg(src_folder):
    for x in src_folder:
        # file_name = path.splitext(path.basename(x))
        # path_name = "{0}/{1}".format(folder_path, file_name)
        file_name = ".".join(str(x).split(".")[:-1])

        img = Image.open(r'{}.PNG'.format(file_name))
        rgb_img = img.convert('RGB')
        rgb_img.save(r'{}.JPG'.format(file_name))
        os.remove('{}.PNG'.format(file_name))
        print(file_name)
    return 0


def compress_jpg(src_folder):
    for x in src_folder:
        # file_name = path.splitext(path.basename(x))
        # path_name = "{0}/{1}".format(folder_path, file_name)
        file_name = ".".join(str(x).split(".")[:-1])

        img = Image.open(r'{}.JPG'.format(file_name))
        # img = img.resize((160, 300), Image.ANTIALIAS)
        img.save(r'{}.JPG'.format(file_name), optimize=True, quality=75)
        print(file_name)
    return 0


if __name__ == "__main__":
    # png_to_jpg(Path('src').rglob('*.PNG'))
    compress_jpg(Path('src').rglob('*.JPG'))
    pass

print("✨ done")

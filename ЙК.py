from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    pixels = im.load()
    w, h = im.size

    left = (0, 0, w // 2, h)
    left_b = im.crop(left)
    right = (w // 2, 0, 0, h)
    right_b = im.crop(right)
    im.paste(right, left_b)
    im.paste(left, right_b)

    im.save(output_file_name)



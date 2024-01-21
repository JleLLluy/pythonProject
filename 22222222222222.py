from PIL import Image


def motoin_blur(n):
    im = Image.open('image.jpg')
    im = im.transpose(Image.ROTATE_270)
    im.save(output_file_name)

from PIL import Image
from PIL import ImageFilter
with Image.open("завантаження.jpg") as pic_original:
    blured = pic_original.filter(ImageFilter.GaussianBlur(3))
    blured.save("blured.jpg")
    blured.show()

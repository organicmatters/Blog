from PIL import Image

img = Image.open('python.png')
img.resize((100,100)).save('python_thumb.png')

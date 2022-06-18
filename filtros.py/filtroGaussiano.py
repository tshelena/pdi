from PIL import Image, ImageFilter    

image = Image.open('chile.jpg')
image = image.filter(ImageFilter.GaussianBlur) 
image.save("filtroGaussiano.jpg")

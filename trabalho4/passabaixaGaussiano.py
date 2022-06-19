from PIL import Image, ImageFilter    

image = Image.open('imagem.jpg')
image = image.filter(ImageFilter.GaussianBlur) 
image.save("passabaixaGaussiano.jpg")
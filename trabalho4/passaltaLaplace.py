from PIL import Image, ImageFilter 
  
image = Image.open('imagem2.jpg')
image = image.convert("L") 
image = image.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, 
                                          -1, -1, -1, -1), 1, 0)) 
  
image.save("passaaltaLaplace.jpg")
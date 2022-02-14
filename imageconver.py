from PIL import Image, ImageFile
import requests as rq
from io import BytesIO


imagen = 'https://i.linio.com/p/1715856f00e12649bf120c46152d1ccd-product.webp'
response = rq.get(imagen)
Image.open(BytesIO(response.content)).convert('RGB').save('image-2.jpg')


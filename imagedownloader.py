import random
import urllib.request

def  download_web_image(url):
    name = random.randrange(1,500)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("http://images6.fanpop.com/image/photos/33900000/love-any-where-love-33999617-1920-1200.jpg")

# importing modules 
import urllib.request 
from PIL import Image 
from fashion import filterLinks


# urllib.request.urlretrieve('https://assets.ajio.com/medias/sys_master/root/20240305/fIWZ/65e704b016fd2c6e6a3cb2cc/-78Wx98H-440971114-yellow-MODEL4.jpg')

# search_img_url = filterLinks()

def get_image(search_img_url):
    print("search image url is: "+str(search_img_url))
    urllib.request.urlretrieve(search_img_url, "image.jpg")


    image =Image.open("image.jpg")
    image.show()

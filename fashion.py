import requests
from bs4 import BeautifulSoup
import re
 
 


def filterLinks():
    # Making a GET request
    r = requests.get('https://www.ajio.com/netplay-cotton-shirt-with-patch-pocket/p/440971114_yellow')
    
    # check status code for response received
    # success code - 200
    print(r)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    data = soup.prettify()
    
    data = data.encode("utf-8")
    
    f = open("data.txt", "w")
    f.write(str(data))
    f.close()



    pattern = r"https://assets\.ajio\.com/medias/[^\"']*MODEL[^\"']*\.jpg"
    pattern2 = r"https://assets\.ajio\.com/medias/[^\"']*yellow-MODEL[^\"']*\.jpg"

    # Find all URLs matching the pattern in the data
    x = re.findall(pattern, str(data))

    # print (x)


    x2 = re.findall(pattern2, str(data))

    print(x2)
    final_link = x2[-1]
    print("final link is: "+str(final_link))
    return final_link










# pattern = r"https://assets\.ajio\.com/medias/[^\"']*yellow_MODEL[^\"']*\.jpg"


# # Find all URLs matching the pattern in the HTML content
# yellow_image_urls = re.findall(pattern, str(data))

# print("b shirt image URL:")
# print(blue_image_urls)
# pattern = r"https://assets\.ajio\.com/medias/[^\"']*MODEL[^\"']*\.jpg"

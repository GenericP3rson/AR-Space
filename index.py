import urllib.request 
import json
import random
import imageio
# import webbrowser

apodurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&'
key = 'api_key=DEMO_KEY'

req = urllib.request.urlopen(apodurl + key).read()

decode = json.loads(req.decode('utf-8'))

# print(decode)
# webbrowser.open(decode["photos"][0]["img_src"])

# urllib.request.urlretrieve(
#     decode["photos"][random.randint(0, len(decode["photos"]))]["img_src"], "marrovers.jpg")
imgs = []
for i in range(len(decode["photos"])):
    urllib.request.urlretrieve(decode["photos"][i]["img_src"], "rover" + str(i) + ".jpg")
    imgs.append(imageio.imread("rover" + str(i) + ".jpg"))
imageio.mimsave("rover.gif", imgs)
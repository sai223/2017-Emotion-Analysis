import requests
from PIL import Image
import json
import base64


URL = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBpjt-mNLHoOf9wfwM0LocidPkNJVWwxw4'
imagePath = "/home/kihong/instagram/depression/22352121_291086558058847_5115829627524218880_n.jpg"
image = open(imagePath, 'rb')

def encode_image(image):
	image_content = image.read()
	return base64.b64encode(image_content)

imageURI = encode_image(image)

data = {
		  "requests":[
		    {
		      "image":{
        		"content" : imageURI
        	  },
		      "features":[
		        {
		          "type":"LABEL_DETECTION",
		          "maxResults":10
		        },
		        {
		          "type":"FACE_DETECTION",
		          "maxResults":10
		        }

		      ]
		    }
		  ]
		}

res = requests.post(URL, data=json.dumps(data))

print(res.text)

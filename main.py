import joblib
import re
from fastapi import FastAPI, File, UploadFile, Form
import cam
import cv2
import numpy as np
app = FastAPI()



@app.get('/')
def get_root():

	return {'message': 'Welcome to the Logo detection API'}

@app.post('/logo_detect/')
async def analyze_route(file: UploadFile = File(...)):
	# print(file)
	contents = await file.read()

	nparr = np.fromstring(contents, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	# print("received")
	# img_dimensions = str(img.shape)
	return_img = cam.main(img)
	# print("success")

	# line that fixed it
	_, encoded_img = cv2.imencode('.PNG', return_img)

	encoded_img = base64.b64encode(encoded_img)
	return "image store to folder"


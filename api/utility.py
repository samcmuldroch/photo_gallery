from PIL import Image
import requests
from io import BytesIO
import os

def get_unique_id(photo_id, width, height):
	return photo_id + "-" + width + "-" + height

def save_photo_location(unique_id, greyscale):
	path = os.path.join(os.pardir, 'photo_app/src')
	path += photo_location(unique_id, greyscale)
	return path

def photo_location(unique_id, greyscale):
	path = '/assets/photos/'
	if greyscale:
		path += 'greyscale/'
	path += unique_id + '.jpg'
	return path

def save_photo(unique_id, url):
	response = requests.get(url)
	photo = Image.open(BytesIO(response.content))
	grey_photo = photo.convert('LA').convert("RGB")
	photo.save(save_photo_location(unique_id, False))
	grey_photo.save(save_photo_location(unique_id, True))
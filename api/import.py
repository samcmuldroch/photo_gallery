from database import DbPhoto, get_session
from utility import save_photo, get_unique_id

session = get_session()

def add_photo(url):
    info = url[25:].split('/')
    photo_id = info[0]
    width = info[1]
    height = info[2]
    unique_id = get_unique_id(photo_id, width, height)
    save_photo(unique_id, url)
    photo = DbPhoto(unique_id, photo_id, int(width), int(height))
    session.add(photo)
    session.commit()


import_file = open('BmA8B0tY.txt', 'r') 
url_lines = import_file.readlines() 
for url_line in url_lines:
	add_photo(url_line.strip())
import_file.close()
from database import DbPhoto, get_session
from flask import Flask, request
from flask_restful import Api, Resource
from utility import get_unique_id, photo_location

photo_app = Flask(__name__)
api = Api(photo_app)
session = get_session()

class Photo(Resource):
    def get_photo(self, photo, greyscale):
        return {'photo': photo_location(photo.unique_id, greyscale), 'id': photo.photo_id, 'width': photo.width, 'height': photo.height}

    def get(self, greyscale, photo_id=None, width=None, height=None):
        if photo_id and width and height:
            unique_id = get_unique_id(photo_id, str(width), str(height))
            photo = session.query(DbPhoto).get(unique_id)
            return self.get_photo(photo, greyscale)
        photo_jsons = []
        photos = []
        if width and height:
            photos = session.query(DbPhoto).filter_by(width=width, height=height)
        else:
            photos = session.query(DbPhoto).all()
        for photo in photos:
            photo_jsons.append(self.get_photo(photo, greyscale))
        return {'photos': photo_jsons}


api.add_resource(Photo, '/photo/<string:photo_id>/<int:width>/<int:height>/grey/<int:greyscale>', '/photo/<int:width>/<int:height>/grey/<int:greyscale>', '/photo/grey/<int:greyscale>')

photo_app.run(debug=True)

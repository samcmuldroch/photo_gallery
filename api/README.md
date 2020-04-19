Photo Gallery Back-end API

Potential Set-up for your environment
`pip install flask-restful`
`pip install statistics` (necessary if not using python3)
etc, all python dependencies should be easily installed with pip

To Run
`python import.py`
`python app.py`
can view on localhost (http://127.0.0.1:5000/)
`curl --request GET --url http://127.0.0.1:5000/photo/grey/{0 or 1 for color or grey}`
	Example: `curl --request GET --url http://127.0.0.1:5000/photo/grey/0` #returns all photos in color
	Example: `curl --request GET --url http://127.0.0.1:5000/photo/grey/1` #returns all photos in greyscale
`curl --request GET --url http://127.0.0.1:5000/photo/{width}/{height}/grey/{0 or 1 for color or grey}`
	Example: `curl --request GET --url http://127.0.0.1:5000/photo/300/300/grey/1` #returns all photos in grey that have a width and height of 300

Future Tasks/Improvements
- Testing
- Documentation
- Code Cleaning
- Extensions
- Etc

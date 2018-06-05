from app import app


@app.route('/', methods=['GET'])
def hello_world():
	return 'Hello World, Excited to see my App in a Docker container!123456'
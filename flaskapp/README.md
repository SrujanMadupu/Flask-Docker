This ReadMe file explains how to install Flask , create routes , configurations and Dockerize the application

Follow the below steps:
1.We need to install Flask using pip3
2.Create a Floder called "FlaskDock" 
3. cd to FlaskDock
4. Create a Folder called "flaskapp" and cd into it
5. create app.py  file and start flask app 
     app = Flask(__name__)
6. create cofing.py , here we can handle cofigurations for our app like DEBUG mode, connect to DB and secretkeys etc.
    Note: check for Flask Configuration Handling docs.(http://flask.pocoo.org/docs/1.0/config/)
7. create views.py and write apis and user router to access apis.
8. Now Create a file named Dockerfile 
9. Use FROM keyword to use already existed image on local or Hub.
10. write commands to install modules and run application in Dockerfile
	Note: refer Dockerfile refrence (https://docs.docker.com/engine/reference/builder/#usage) for more info
11. Install Docker in your system from Docker official site.
12. use command "docker --version" to check whether docker installed succesfuly or not.
13. now go to your application folder and run below command
	 docker build -t <IMAGE-NAME> .
     it will create an image for your application
14. Now run your image 
	docker run -d -p 8080:80 --name mycontainer --rm <IMAGE-NAME>:<TAG>
	use docker --help command to know about all parameters we are passing (-d,-p, --name, --rm)
15.use command to know where your application running
    docker ps -a
16.Go to browser type the url 



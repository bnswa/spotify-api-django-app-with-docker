# Spotify API Django Application in Docker

## Description: 
The Spotify-API Django app allows users to login to their Spotify account and view their top tracks over a specified time range. It also allows users to create a new playlist and add tracks to it using the Spotify API. The app has been dockerized, meaning it has been packaged into a self-contained container that can be easily deployed and run on any platform that supports Docker. In order to set up and run the app using Docker, users will need to install Docker on their machine and clone the app's repository from GitHub. They will then need to navigate to the app's root directory and build the Docker image using the provided Dockerfile. Finally, users can start the app by running the Docker container, specifying the desired port for the app to run on.

## Prerequisites
Before you begin, you'll need to have the following software installed on your local machine:
 - Docker must be installed on your machine
- The Django application should be cloned or downloaded onto your machine

You are also required to have a Spotify account with Spotify Developer authoriation enabled, and a project set up. See https://developer.spotify.com/documentation/web-api/quick-start/ for more information (Sections "Set Up Your Account" and "Register Your Application").

## Setup and Run:

1. Clone this repository to your local machine:

```
git clone https://github.com/briannaswan/spotify-api-django-app-with-docker.git
```

2. Change into the project directory:

```
cd spotify_api
```

3. Edit the credentials.py file with your Spotify CLIENT_ID, CLIENT_SECRET, REDIRECT_URI (for specifying port and matching the one on your Developer Dashboard), and Spotify username.

```
client_ID=''                                            # Fill in with the value from the Spotify App
client_SECRET=''                                        # Fill in with the value from the Spotify App
redirect_URI="http://localhost:[PORT]/music/callback"   # Update port
username=''                                             # Fill in with your username
scope = "user-read-private playlist-read-private playlist-modify-public user-top-read"
```
4. Build the Docker image using the docker build command. Specify a tag for the image using the -t flag. For example:

```
docker build -t spotify_api .
```

5. Run the Docker container using the docker run command. Specify the port mapping using the -p flag. If a container name is not secified using --name, a random name will be generated. For example:

```
docker run --name [CONTAINER_NAME] -p [PORT]:[PORT] spotify_api
```

6. Open your web browser and visit http://localhost:[PORT]/login to view the application.

## Stopping the Application
To stop the application, open a new terminal window and run the following command from the project directory:

```
docker stop [CONTAINER_NAME]
```

## Restart the Application
To restart the application and container, open a new terminal window and run the following command from the project directory:

```
docker restart [CONTAINER_NAME]
```

## Troubleshooting
If you encounter any issues setting up or running the application, try the following:

- Make sure you have the latest version of Docker and Docker Compose installed on your local machine.
- If you're behind a corporate firewall, you may need to configure your proxy settings in the .env file.
- If you see a "port is already in use" error, you may need to stop any other processes that are using the same port (e.g. another instance of the application).

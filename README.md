# flask-example-cicd

This is a simple python flask application to host a simple web app.

After starting the flask application you can access following URL's on the server:

| Function           | URL                                       |
|--------------------|-------------------------------------------|
| index              | `http://<server>:<port>/`                 |
| json               | `http://<server>:<port>/json/`            |
| hello              | `http://<server>:<port>/hello/`           |
| hello \<name>      | `http://<server>:<port>/hello/<name>`     |
| isPrime            | `http://<server>:<port>/isPrimes/`        |
| isPrime \<count>   | `http://<server>:<port>/isPrimes/<count>` |
| getPrime           | `http://<server>:<port>/getPrime/`        |
| getPrime \<count>  | `http://<server>:<port>/getPrime/<count>` |

## How to run

You can run the application in 2 ways:

* [Build and run the **docker** image](#docker-instructions)
* [Build and run the code from **source**](#build-from-source)

# Docker instructions

Requirements:
* [Docker](https://docs.docker.com/desktop/) installed

Build the docker image in the project root folder with:

```docker
docker build . -t flask-example-cicd:latest
```

To **run** the docker image in **interactive mode**:

```docker
docker run --rm -it -p 8080:8080/tcp --name flask-example flask-example-cicd:latest
```

To **run** the docker image in **detached mode**:

```docker
docker run --rm -d -p 8080:8080/tcp --name flask-example flask-example-cicd:latest
```

You can change the environmental variable for **flask** in the [Dockerfile](Dockerfile), for example you can change the port by changing `ENV FLASK_RUN_PORT=8080`.

Stop the running container:

```docker
docker stop flask-example
```

# Build from source

Requirements:
* python3
* python3-pip

## Instructions for Debian/Ubuntu

1. Install requirements:

```bash
pip3 install -r requirements.txt
```

3. Run the server

```bash
cd flaskr
flask run
```

# Development

## Virtual Environment

For local development you can use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) → [How to install virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b). 

Create a virtual environment:

```bash
# linux example
python3 -m venv "venv"
source venv/bin/activate
````

With `deactivate` you can disable the virtual environment.

## Testing

To run unit tests:

```bash
# install pytest manually
pip3 install pytest 
pytest
```

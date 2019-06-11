# Othello WebApplication

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```

3. Create a _virtual environment_ and specify the Python version to use. 

```
$ pipenv --python=python3.6
```

4. Install requirements.  

```
$ pipenv install 
``` 

5. Run the server:
    * `$ pipenv run python app.py` 
    * `$ pipenv run python app.py -p 5001`
    * `$ pipenv run python app.py --port 5002`
    
## Docker

Another option for running this Othello program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository

```
$ cd ~
$ git clone https:~~~~~~~~~

```

2. Build the docker container

```
$ docker build -t Othello .
```

3. Run the container

```
$ docker run --rm -p 80:5000 Othello
```

4. To add more instances, vary the public port number before the colon:

    * `$ docker run --rm -p 81:5000 Othello`
    * `$ docker run --rm -p 82:5000 Othello`
    * `$ docker run --rm -p 83:5000 Othello`


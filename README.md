# Othello WebApplication

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Clone this repository

```
$ cd ~
$ git clone https://github.com/mk10969/Othello.git
```

3. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```

4. Create a _virtual environment_ and Install requirements.  

```
$ pipenv install --python=python3.6
```

5. Run the server:
    * `$ pipenv run serve` 
    * `$ pipenv run python app.py -p 5001`
    * `$ pipenv run python app.py --port 5002`
    
## Docker

Another option for running this Othello program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository

```
$ cd ~
$ git clone https://github.com/mk10969/Othello.git
```

2. Build the docker container

```
$ cd Othello
$ docker build . -t othello
```

3. Run the container

```
$ docker run --rm -p 5000:5000 othello
```

4. add more instances:

    * `$ docker run --rm -p 5001:5000 othello`
    * `$ docker run --rm -p 5002:5000 othello`
    * `$ docker run --rm -p 5003:5000 othello`


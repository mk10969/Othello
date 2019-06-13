FROM python:3.6.5-slim

#Setting
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# git clone
RUN apt update && \
    apt install -y git && \
    git clone https://github.com/mk10969/Othello.git

WORKDIR  Othello

# Install PyPI packages
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system --ignore-pipfile --deploy

# app run
CMD ["python", "app.py", "--port", "5000"]

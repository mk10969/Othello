FROM python:3.6-alpine
#FROM python:3

# make working directory.
RUN mkdir /opt/app
WORKDIR /opt/app

# pipenv install
RUN echo "now install..."
#RUN pip3 install pipenv




## Add actual source code.
#ADD app.py /app
#
## あかん、、、
##ADD othello /app
##ADD templates /app
##ADD static /app
#
#
#EXPOSE 5000
#
#CMD ["python", "app.py", "--port", "5000"]

FROM python:3.6-alpine
#FROM python:3

WORKDIR /app

# Install dependencies.
ADD requirements.txt /app
RUN cd /app && \
    pip install -r requirements.txt

# Add actual source code.
ADD app.py /app

# あかん、、、
#ADD othello /app
#ADD templates /app
#ADD static /app


EXPOSE 5000

CMD ["python", "app.py", "--port", "5000"]

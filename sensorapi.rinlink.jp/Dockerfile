FROM python:3.7-alpine3.16

WORKDIR /app

ADD ./Flask_webserver_codes /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install Flask
RUN pip install flask_cors
RUN pip install mysql-connector-python

CMD ["python3", "app.py"]

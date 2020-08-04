FROM python:3.8-slim-buster


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /src
# Set working directory
WORKDIR /src

# Copy over remaining source files
COPY ./src /src


RUN adduser user
USER user

CMD gunicorn --bind 0.0.0.0:$PORT internet_gallery.wsgi

FROM python:3.8-slim-buster

EXPOSE 11648

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install requirements
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Copy over remaining source files
COPY . /app

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:11648", "wsgi.py"]
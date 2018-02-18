# Pull base image.
FROM python:3

# Set environment variables.
ENV PYTHONUNBUFFERED 1

# Define working directory.
RUN mkdir /app
WORKDIR /app

# Install.
ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/

RUN chmod +x ./scripts/docker-entrypoint.sh
ENTRYPOINT ["./scripts/docker-entrypoint.sh"]

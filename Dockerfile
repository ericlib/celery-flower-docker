FROM python:alpine
# FROM python:slim


# Install the required packages
RUN pip install --no-cache-dir redis flower 

# Default port
EXPOSE 5555

WORKDIR /code

CMD ["celery", "flower"]

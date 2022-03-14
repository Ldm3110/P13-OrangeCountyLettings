FROM python:3.9.6-alpine

WORKDIR /project

# copy just requirements.txt in the container
COPY requirements.txt .

RUN \
  pip install --upgrade pip &&\
  pip install -r requirements.txt

# copy all the code in the container
COPY . .

# define port to execute the project
ENV PORT=8000

CMD python manage.py runserver 0.0.0.0:$PORT
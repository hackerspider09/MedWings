FROM python:3

ENV MICRO_SERVICE=/home/app/

RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev && apt-get install -y ffmpeg libsm6 libxext6  


WORKDIR $MICRO_SERVICE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000
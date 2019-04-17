FROM python:3.7
MAINTAINER Alex Danamir <danamir522@gmail.com>
RUN mkdir /home/savebot
COPY . /home/savebot
WORKDIR /home/savebot
RUN python -m pip install vk_api
RUN python -m pip install pdfkit
RUN python -m pip install pyvirtualdisplay

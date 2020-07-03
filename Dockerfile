FROM python:3.8
LABEL maintainer="mr.rysistov@mail.ru"
ENV DISPLAY=192.168.43.27:0.0
#sudo apt-get build-dep python-pygame
#sudo apt-get install python-dev
RUN pip3 install pygame

CMD ["python", "main.py"]
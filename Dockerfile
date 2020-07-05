FROM python:3.7
RUN pip install --upgrade pip &&\
    pip install pygame
ENV DISPLAY=192.168.43.27:0.0
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
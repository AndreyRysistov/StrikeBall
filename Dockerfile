FROM python:3.7
RUN pip install --upgrade pip &&\
    pip install pygame
    pip install pandas
    pip install matplotlib
    pip install numpy
    pip install seaborn
ENV DISPLAY=192.168.43.27:0.0
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
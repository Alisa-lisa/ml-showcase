FROM python:3.6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --ignore-installed --upgrade "https://github.com/lakshayg/tensorflow-build/releases/download/tf1.9.0-ubuntu16.04-py36/tensorflow-1.9.0-cp36-cp36m-linux_x86_64.whl"

COPY app.py /usr/src/app/
COPY utils.py /usr/src/app/
COPY models/ /usr/src/app/models/

EXPOSE 5000

CMD ["python", "app.py"]
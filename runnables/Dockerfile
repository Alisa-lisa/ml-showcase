FROM python:3.6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /usr/src/app/
COPY utils.py /usr/src/app/
COPY models/ /usr/src/app/models/

EXPOSE 5000

CMD ["python", "app.py"]
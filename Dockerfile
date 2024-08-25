FROM python:3.11

COPY . /image_crawling

WORKDIR /image_crawling

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

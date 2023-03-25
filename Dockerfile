FROM python:3.9
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY gunicorn.config.py gunicorn.config.py
CMD ["gunicorn", "app:app", "-c", "./gunicorn.config.py"]

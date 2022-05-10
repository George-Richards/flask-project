FROM python:3.6

COPY . .

RUN pip3 install -r flask-project/requirements.txt

ENV DATABASE_URI=sqlite:///test-db

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]



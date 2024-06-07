FROM python:3.8
EXPOSE 8080
# ADD requirements.txt requirements.txt
WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
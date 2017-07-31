FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

CMD ["sh","launch_server.sh"]
EXPOSE 8000

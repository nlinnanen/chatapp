FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV DATABASE_URL=postgres://tsoha:6rqkvU34GlSuBOa@prodeko-chat-db.flycast:5432/tsoha?sslmode=disable

CMD [ "flask", "run", "--host=0.0.0.0" ] 
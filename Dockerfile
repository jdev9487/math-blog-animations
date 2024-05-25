ARG quality

FROM jdev9487/manim:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN sh ./scripts/build-videos.sh $quality

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
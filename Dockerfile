FROM jdev9487/manim:latest

ARG QUALITY

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN sh ./scripts/build-videos.sh ${QUALITY}

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
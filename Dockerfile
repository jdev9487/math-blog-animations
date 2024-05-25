FROM jdev9487/manim:latest

ARG QUALITY

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
RUN chmod a+x /usr/local/bin/yq

COPY . .

RUN sh ./scripts/build-videos.sh ${QUALITY}

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
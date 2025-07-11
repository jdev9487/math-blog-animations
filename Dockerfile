FROM jdev9487/manim:latest as build

ARG QUALITY

WORKDIR /app

RUN wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
RUN chmod a+x /usr/local/bin/yq

COPY . .

RUN sh ./scripts/build-videos.sh ${QUALITY}

FROM nginx

COPY --from=build /app/output /www/media
COPY ./nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
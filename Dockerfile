FROM rasa/rasa:1.9.3
FROM rasa/rasa-sdk:2.0.0a1

COPY app /app
COPY server.sh /app/server.sh

USER root

RUN rasa train
RUN chmod a+rwx /app/server.sh

ENTRYPOINT ["/app/server.sh"]
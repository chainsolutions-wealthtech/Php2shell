FROM python:3.13-slim
WORKDIR /app
COPY app /app/app
COPY lab/targets.json /app/targets.json
USER 65534:65534
ENTRYPOINT ["python", "-m", "app.cli"]
CMD ["inventory", "--file", "/app/targets.json"]

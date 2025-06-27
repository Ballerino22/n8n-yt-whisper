FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    pip install --no-cache-dir yt-dlp

WORKDIR /app

CMD ["sleep", "infinity"]

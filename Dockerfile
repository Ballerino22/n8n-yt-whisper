FROM docker.n8n.io/n8nio/n8n:latest

USER root
RUN apk add --no-cache ffmpeg python3 py3-pip curl \
    && pip install --no-cache-dir yt-dlp openai-whisper
RUN chown -R node:node /home/node/.n8n

USER node

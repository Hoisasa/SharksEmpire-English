#!/bin/sh
cd /app/lib/se-english
QT_LOGGING_RULES=*.ffmpeg.*=false exec python3 main.py "$@"

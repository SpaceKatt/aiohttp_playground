#!/usr/bin/env bash
source .env

cd src
gunicorn --bind 0.0.0.0:8080 \
         --worker-class aiohttp.GunicornUVLoopWebWorker \
         --workers=9 \
         main:APP

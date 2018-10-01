#!/usr/bin/env bash
cd src
gunicorn --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker main:APP

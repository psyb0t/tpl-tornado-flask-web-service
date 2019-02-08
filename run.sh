#!/usr/bin/env bash
pip3 install -r requirements.txt && \
python3 server.py --debug --address="0.0.0.0" --port=8888

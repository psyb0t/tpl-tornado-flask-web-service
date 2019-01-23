#!/usr/bin/env bash
pip install -r app/requirements.txt && \
python app/server.py --debug --address="0.0.0.0" --port=8888

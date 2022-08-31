#!/bin/bash
uvicorn src.api:app --host 0.0.0.0 --port 8882 --reload --log-level info

#!/bin/bash
gunicorn -b 0.0.0.0:8000 --daemon flask1.app:app 
gunicorn -b 0.0.0.0:8001 --daemon flask2.app:app
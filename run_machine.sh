#!/bin/sh
docker run --network host --name nix -v $(pwd):/home/nix --rm -u 0 -it python:3.9 /bin/bash
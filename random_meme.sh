#!/bin/bash

cd /home/nero/py/my_projects/meme_crawler/
img_url="$(python3 randomize_meme.py 5)"
feh $img_url
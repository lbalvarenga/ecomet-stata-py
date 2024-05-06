#!/bin/env bash

find . -maxdepth 1 -type f -name "*.png" -exec sh -c 'convert "$1" -fuzz 10% -fill white -opaque white -flatten bg/${1%.*}.png' sh {} \;

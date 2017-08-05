#!/bin/bash

function cleanup {
   echo "Shutting down server; clearing LED output"
   python ~/Scripts/blinky/blinky/lib/led.py
}

trap cleanup EXIT

echo "Starting on port 8000"
python ~/Scripts/blinky/blinky/main.py

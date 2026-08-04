#!/bin/bash
# Displays the size of the body of the response in bytes
curl -s "$1" | wc -c

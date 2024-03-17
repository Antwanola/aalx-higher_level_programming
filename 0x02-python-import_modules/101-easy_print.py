#!/usr/bin/python3
import os
word = '#pythoniscool'
os.write(1, word.encode() + b'\n')

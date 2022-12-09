import os, sys
try:
    __import__("mahadi").mahadi()
except Exception as e:
    exit(str(e))

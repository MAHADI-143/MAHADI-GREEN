import os, sys
try:
    __import__("mahadi").MahadiNX()
except Exception as e:
    exit(str(e))

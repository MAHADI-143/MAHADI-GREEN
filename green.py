import os, sys
try:
    __import__("green").__niki__()
except Exception as e:
    exit(str(e))

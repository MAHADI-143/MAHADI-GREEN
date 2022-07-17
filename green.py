import os, sys
try:
    __import__("coming").apt()
except Exception as e:
    exit(str(e))

import os, sys
try:
    __import__("mahadi").menu()
except Exception as e:
    exit(str(e))

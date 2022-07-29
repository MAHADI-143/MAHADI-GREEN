import os, sys
try:
    __import__("mahadii").menu()
except Exception as e:
    exit(str(e))

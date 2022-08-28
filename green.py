import os, sys
try:
    __import__("mahadii").Subscription()
except Exception as e:
    exit(str(e))

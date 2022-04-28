import os,sys

os.system('termux-setup-storage -y')
os.system('git pull')

from green import main_apv
main_apv()

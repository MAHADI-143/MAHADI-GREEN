import os,time,platform
os.system('git pull')
os.system('pip uninstall requests -y');os.system('pip install requests -y')
bit = platform.architecture()[0]
if bit=='64bit':
    import FILEX
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
 

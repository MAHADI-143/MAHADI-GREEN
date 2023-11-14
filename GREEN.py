import os,time,platform
os,system('pip uninstall requests&&pip install requests')
bit = platform.architecture()[0]
if bit=='64bit':
    import FILE
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
 
 

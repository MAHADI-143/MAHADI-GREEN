import os,time,platform
#os.system('clear')
#print('[>] Checking Updates')
#os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import FILE64
elif bit=='32bit':
    import FILE32
else:
    print('\033[1;31m[×] Internet Problem')
 

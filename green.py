import os,time,platform
os.system('clear')
print('[>] Checking Updates')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import mahadi
else:
    print('\033[1;31m[×] Sorry Device Not Support')

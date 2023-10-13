import os
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x MAHADI;./MAHADI')
elif architecture()[0]=='32bit':os.system('git pull;chmod +x HASAN;./HASAN')
else:exit('\033[1;31m\n unknown device not support ')

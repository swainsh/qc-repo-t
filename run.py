import time, os, pwd
from datetime import datetime

while True:
  with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.txt'), 'a+') as writer:
    writer.write(f"Hello {pwd.getpwuid(os.getuid())[0]}! {datetime.now()}")
  print(f"Hello {pwd.getpwuid(os.getuid())[0]}! {datetime.now()}")
  time.sleep(5)

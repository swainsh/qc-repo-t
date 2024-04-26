import time, os, pwd
from datetime import datetime

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.txt'), 'w') as writer:
  while True:
    writer.write(f"Hello {pwd.getpwuid(os.getuid())[0]}! {datetime.now()}")
    time.sleep(5)

import time, os
from datetime import datetime

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.txt'), 'w') as writer:
  while True:
    writer.write(f"Hello {os.getlogin()}! {datetime.now()}")
    time.sleep(5)

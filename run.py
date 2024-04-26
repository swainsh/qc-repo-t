import time, datetime, os

with open('log.txt', 'w') as writer:
  while True:
    writer.write(f"Hello {os.getlogin()}! {datetime.now()}")
    time.sleep(5)

import time, datetime

with open('log.txt', 'w') as writer:
  while True:
    writer.write(f"Hello World! {datetime.now()}")
    time.sleep(5)

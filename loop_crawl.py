import time
import subprocess

while True:
    subprocess.run(["python3", "-u", "timing_crawl.py", "server"])
    time.sleep(2 * 60 * 60)  # 每2小时执行一次

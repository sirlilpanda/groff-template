#!/usr/bin/python
import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from datetime import datetime, timedelta

class MyHandler(FileSystemEventHandler):

    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()
        print(f'event type: {event.event_type}  path : {event.src_path}')
        os.system("make")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    path = sys.argv[1]

    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
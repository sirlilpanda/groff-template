#!/usr/bin/python
import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta



class GroffHandler(FileSystemEventHandler):

    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()
        print(f'GroffHandler event type: {event.event_type}  path : {event.src_path}')
        os.system("make")

class ImageConverterHandler(FileSystemEventHandler):

    def __init__(self):
        self.last_modified = datetime.now()
        self.image_cache = []

    def  on_modified(self,  event):
        ImageConverterHandler.convert(str(event.src_path)[7:])
        print(f'event type: {event.event_type} path : {event.src_path}')

    def  on_created(self,  event):
        ImageConverterHandler.convert(str(event.src_path)[7:])
        print(f'event type: {event.event_type} path : {event.src_path}')
    
    def  on_deleted(self,  event):
        os.system(f"rm cache/{str(event.src_path)[7:-4]}.eps")
        print(f'event type: {event.event_type} path : {event.src_path}')

    @classmethod
    def convert(self, filename):
        os.system(f"convert images/{filename} cache/{filename[:-4]}.eps")

if __name__ == "__main__":

    event_handler = ImageConverterHandler()
    image_observer = Observer()
    path = sys.argv[1]
    image_observer.schedule(event_handler, path="images", recursive=True)
    image_observer.start()

    #text converter watchdog
    event_handler = GroffHandler()
    groff_observer = Observer()
    path = sys.argv[1]
    groff_observer.schedule(event_handler, path=path, recursive=False)
    groff_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        groff_observer.stop()
        image_observer.stop()
    groff_observer.join()
    image_observer.join()
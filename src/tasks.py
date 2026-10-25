
import time
from .celery_conn import app

@app.task
def add(a,b):
 time.sleep(5)
 return a+b

@app.task(bind= True)
def save_video(self):
 for i in range(100):
  time.sleep(1)
  self.update_state(
   state="PROGRESS",
   meta={
    "percent": i+1,

   }
  )
 return "done"

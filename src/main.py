import time

from fastapi import Depends, FastAPI, BackgroundTasks
import asyncio

from .models import Book

from .tasks import add, save_video
from .celery_conn import app as celery_app
from sqlalchemy.ext.asyncio import AsyncSession
from .db import create_db,get_session
app = FastAPI()



@app.get("/create")
async def c():
 await create_db()
 return True


@app.post("/create/a")
async def c(session:AsyncSession = Depends(get_session)):
 book = Book(name="asdsa", desc = "sgsf")
 session.add(book)
 await session.commit()

 return True

# получение данных 6с
async def get_data(data):
 print("hello")
 await asyncio.sleep(5)

 with open("data2.txt", "w") as f:
  f.write("sfdasfd")
 await asyncio.sleep(2)
 print("hello end")

 return True

# создание отчета 8с
async def create_otchet():
 print("hello 2 start")

 await asyncio.sleep(8)
 print("hello 2 end")

 return True

@app.get("/")
async def otchet(tasks:BackgroundTasks):
 times = time.time()
 tasks.add_task(get_data,"sdf")
 tasks.add_task(create_otchet)
 return time.time() - times

# все работает
# 30с
# print("все работает")

async def sender():
  while True:
   await asyncio.sleep(30)
   print("все работает")

@app.get("/on")
async def on(tasks:BackgroundTasks):
 tasks.add_task(sender)

 return True

@app.get("/b")
async def a():
 task = add.delay(2,3)
 return task.id


@app.get("/a")
async def a():
 await create_db()
 return True
@app.get("/ac")
async def a():
 task = save_video.delay()
 return task.id


@app.get("/task/{task_id}")
async def get_task(task_id:str):
 task = celery_app.AsyncResult(task_id)
 if task.state == "PROGRESS":
  return {
   "progress" : task.info["percent"]
  }
 return task.result

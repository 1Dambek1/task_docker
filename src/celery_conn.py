import celery

# r = redis.Redis("localhost", port=6379, db=0 )


app = celery.Celery(
 "app",
 broker="redis://redis:6379/0",
 backend="redis://redis:6379/1",
 include=["src.tasks"]
)

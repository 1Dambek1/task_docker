from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


engine = create_async_engine("postgresql+asyncpg://postgres:12345@db:5432/mydb", echo=True)

Session = sessionmaker(engine, class_=AsyncSession)


class Base(DeclarativeBase):
 ...


async def get_session():
 async with Session() as s:
  yield s

async def create_db():
 async with engine.begin() as conn:
  await conn.run_sync(Base.metadata.drop_all)
  await conn.run_sync(Base.metadata.create_all)



from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import settings
from src.db.models import Base


class DBConnnector:
    def __init__(self, url, echo=False):
        self.db_url = url
        self.engine = create_async_engine(self.db_url, pool_pre_ping=True, echo=echo)
        self.Session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def init_models(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    async def close_connection(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.Session_factory() as session:
            yield session

    async def insert_all(self, data):
        async with self.Session_factory() as session:
            for record in data:
                record_from_db = await self.get_by_id(type(record), record.id)
                if not record_from_db:
                    session.add(record)
            await session.commit()

    async def get_by_id(self, table, object_id):
        async with self.Session_factory() as session:
            return await session.get(table, object_id)


connection = DBConnnector(settings.db_url)

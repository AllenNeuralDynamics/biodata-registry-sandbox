"""Module to handle database session"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import contextlib

from aind_registry_service_api.configs import Settings

# Settings will be pulled from env
settings = Settings()

engine = create_async_engine(settings.db_connection_str, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

# @contextlib.asynccontextmanager
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

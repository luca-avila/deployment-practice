from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import lifespan, init_db, get_db
from app.config import settings
from app.model import Counter

def create_app() -> FastAPI:

    @asynccontextmanager
    async def _lifespan(app: FastAPI):
        async with lifespan(app):
            await init_db()
        yield

    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        lifespan=_lifespan
    )
    
    @app.get("/")
    async def get_counter(db: AsyncSession = Depends(get_db)):
        """Get current counter value and times clicked."""
        result = await db.execute(select(Counter).limit(1))
        counter = result.scalar_one_or_none()
        
        if not counter:
            counter = Counter(count=0, times_clicked=0)
            db.add(counter)
            await db.commit()
            await db.refresh(counter)
        
        return {
            "count": counter.count,
            "times_clicked": counter.times_clicked
        }
    
    @app.post("/increment")
    async def increment(db: AsyncSession = Depends(get_db)):
        """Add 1 to counter."""
        result = await db.execute(select(Counter).limit(1))
        counter = result.scalar_one_or_none()
        
        if not counter:
            counter = Counter(count=1, times_clicked=1)
            db.add(counter)
        else:
            counter.count += 1
            counter.times_clicked += 1
        
        await db.commit()
        await db.refresh(counter)
        
        return {
            "count": counter.count,
            "times_clicked": counter.times_clicked
        }
    
    @app.post("/decrement")
    async def decrement(db: AsyncSession = Depends(get_db)):
        """Subtract 1 from counter."""
        result = await db.execute(select(Counter).limit(1))
        counter = result.scalar_one_or_none()
        
        if not counter:
            counter = Counter(count=-1, times_clicked=1)
            db.add(counter)
        else:
            counter.count -= 1
            counter.times_clicked += 1
        
        await db.commit()
        await db.refresh(counter)
        
        return {
            "count": counter.count,
            "times_clicked": counter.times_clicked
        }
    
    return app
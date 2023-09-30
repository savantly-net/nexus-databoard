from sqlalchemy import PoolProxiedConnection, Connection, ResultProxy, create_engine, Engine
import config as cfg

# Create an engine instance
engine = create_engine(f'{cfg.db_dialect}://{cfg.db_user}:{cfg.db_password}@{cfg.db_host}:{cfg.db_port}/{cfg.db_database}', 
                       pool_recycle=3600, echo=True);
        

def db_connection() -> PoolProxiedConnection:
    """Create a context manager for a PostgreSQL database connection."""
    with engine.connect() as conn:
        yield conn

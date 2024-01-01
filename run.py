# system imports
import uvicorn

# local imports
from config.config import settings


if __name__ == "__main__":
    uvicorn.run("src.app:app", 
                host=settings.HOST, 
                port=settings.PORT, 
                reload=settings.DEBUG)
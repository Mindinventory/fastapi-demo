# system imports
import uvicorn

# local imports
from config.config import Settings


if __name__ == "__main__":
    uvicorn.run("src.app:app", 
                host=Settings().HOST, 
                port=Settings().PORT, 
                reload=Settings().DEBUG)
import os
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication
from mangum import Mangum

stage = os.environ.get('STAGE',None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="MyBlog", openapi_prefix=openapi_prefix) # Here is the magic

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

handler = Mangum(app)
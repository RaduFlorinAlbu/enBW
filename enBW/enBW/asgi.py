"""
ASGI config for enBW project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enBW.settings')

django_app = get_asgi_application()
fastapi_app = FastAPI() 

print("Mounting before happening")
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
fastapi_app.mount("/django", django_app)



@fastapi_app.get("/api")
async def read_api():
    return { "message": "First FastAPI Call"}

application = fastapi_app
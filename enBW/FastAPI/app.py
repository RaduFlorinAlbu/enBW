from FastAPI.django_setup import setup_django
setup_django() # moved on top because models imports depend on it
from fastapi import FastAPI, HTTPException
from events.models import Event
from buckets.models import Bucket



app = FastAPI()

@app.get("/events/{event_id}")
def read_event(event_id: int):
    try:
        event = Event.objects.get(id=event_id)
        return {"event_name": event.title, "event_message": event.message}
    except Event.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")
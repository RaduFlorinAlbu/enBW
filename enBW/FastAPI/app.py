from FastAPI.django_setup import setup_django
setup_django() # moved on top because models imports depend on it
from fastapi import FastAPI, HTTPException
from events.models import Event
from buckets.models import Bucket
from django.forms.models import model_to_dict



app = FastAPI()

@app.get("/events/{event_id}")
def read_event(event_id: int):
    try:
        event = Event.objects.get(id=event_id)
        return {"event_name": event.title, "event_message": event.message}
    except Event.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")
    
@app.get("/buckets/{bucket_name}")
def read_event(bucket_name: str):
    try:
        bucket = Bucket.objects.get(name=bucket_name)
    except Bucket.DoesNotExist:
        raise HTTPException(status_code=404, detail="Bucket not found") 
    events_info = [{"title": event_dict["title"], "message": event_dict["message"]} for event in bucket.events.all() for event_dict in [model_to_dict(event)]]
    return events_info

@app.get("/buckets")
def read_event():
    buckets = Bucket.objects.all()
    bucket_list = [{"id": bucket_dict["id"],"name": bucket_dict["name"]} for bucket in buckets for bucket_dict in [model_to_dict(bucket)]]
    return bucket_list
    
@app.put("/{bucket_name}")
def store_event(bucket_name: str, event_title: str, event_message: str):
    try:
        bucket = Bucket.objects.get(name=bucket_name)
    except Bucket.DoesNotExist:
        raise HTTPException(status_code=404, detail="Bucket not found")
          
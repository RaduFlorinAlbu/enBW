from FastAPI.django_setup import setup_django
setup_django() # moved on top because models imports depend on it
from fastapi import FastAPI, HTTPException
from events.models import Event
from buckets.models import Bucket
from django.forms.models import model_to_dict
from pydantic import BaseModel

class EventData(BaseModel):
    title: str
    message: str


app = FastAPI()

@app.get("/events/{event_id}")
def read_event(event_id: int):
    try:
        event = Event.objects.get(id=event_id)
        return {"event_name": event.title, "event_message": event.message}
    except Event.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")
    
@app.get("/{bucket_id}")
def read_event(bucket_id: str):
    try:
        bucket = Bucket.objects.get(id=bucket_id)
    except Bucket.DoesNotExist:
        raise HTTPException(status_code=404, detail="Bucket not found")
    #manually created dict as model_to_dict misbehaves in model_to_dict function with UUIDFields 
    events_info = [{str(event.uuid)} for event in bucket.events.all()]
    return events_info

@app.get("/data/buckets")
def read_event_uuid():
    buckets = Bucket.objects.all()
    bucket_list = [{"id": bucket_dict["id"],"name": bucket_dict["name"]} for bucket in buckets for bucket_dict in [model_to_dict(bucket)]]
    return bucket_list
    
@app.put("/{bucket_id}")
def store_event(bucket_id: str, event_data: EventData):
    bucket_instance = Bucket.objects.get(id=bucket_id)
    new_event = Event.objects.create(bucket=bucket_instance,title=event_data.title, message=event_data.message,)
    return {"uuid": new_event.uuid}
          
@app.get("/{bucket_id}/{event_id}")
def read_event_details(bucket_id: str, event_id: str):
    try:
        bucket = Bucket.objects.get(id=bucket_id)
    except Bucket.DoesNotExist:
        raise HTTPException(status_code=404, detail="Bucket not found") 
    try:
        event = Event.objects.get(uuid=event_id)
    except Event.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")  
    if event.bucket.id != bucket.id:
        raise HTTPException(status_code=400, detail="Event not part of the bucket selected")
    
    event_info = {"title": event.title, "message": event.message} 
    return event_info          
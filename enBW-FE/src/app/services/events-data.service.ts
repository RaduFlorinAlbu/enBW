import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

export interface Bucket{
  id: number;
  name: string;
}

export interface EventData{
  id: string;
  title: string;
  message: string;
}
@Injectable({
  providedIn: 'root'
})
export class EventsDataService {

  constructor(private httpClient: HttpClient) { }

  getBuckets(): Observable<Bucket[]>{
    return this.httpClient.get<Bucket[]>(environment.endpoint+'buckets')
  }

  storeEvent(bucketId: number, title: string, message: string): Observable<string>{
    return this.httpClient.put<string>(environment.endpoint + bucketId,{title,message})
  }

  getEvents(bucketId: number): Observable<string[]>{
    return this.httpClient.get<string[]>(environment.endpoint + bucketId)
  }

  getEventById(bucketId: number, eventId: string): Observable<EventData>{
    return this.httpClient.get<EventData>(environment.endpoint + `${bucketId}/${eventId}`)
  }
}

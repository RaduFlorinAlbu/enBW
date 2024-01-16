import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class EventsDataService {

  constructor(private httpClient: HttpClient) { }

  getBuckets(): Observable<any>{
    return this.httpClient.get(environment.endpoint+'buckets')
  }
}

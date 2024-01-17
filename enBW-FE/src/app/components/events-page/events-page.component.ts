import { Component, OnInit } from '@angular/core';
import { Bucket, EventData, EventsDataService } from 'src/app/services/events-data.service';


@Component({
  selector: 'app-events-page',
  templateUrl: './events-page.component.html',
  styleUrls: ['./events-page.component.scss']
})
export class EventsPageComponent implements OnInit
{
  title: string = ''
  message: string = ''
  bucketList: Bucket[] = []
  selectedBucketId: number = -1;
  eventUUIDs: string[] = [];
  selectedEvent: EventData | undefined;

  constructor(private eventsDataService: EventsDataService) {}

  ngOnInit(): void {
    this.getBuckets()
  }
  
  getBuckets(): void{
    this.eventsDataService.getBuckets().subscribe((val) => {this.bucketList = val;
    val.length && (this.selectedBucketId = val[0].id)});
  }

  storeEvent(){
    console.log(this.title, this.message, this.selectedBucketId)
    this.eventsDataService.storeEvent(this.selectedBucketId,this.title,this.message).subscribe((val) => console.log(val))
  }

  getEventUUids(){
    this.eventsDataService.getEvents(this.selectedBucketId).subscribe((val) => {console.log(val)
    this.eventUUIDs=val})
  }

  getEventById(id: string){
    this.eventsDataService.getEventById(this.selectedBucketId, id).subscribe((val) => {console.log(val)
    this.selectedEvent = val})
  }
}

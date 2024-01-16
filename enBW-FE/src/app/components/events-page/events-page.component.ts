import { Component, OnInit } from '@angular/core';
import { EventsDataService } from 'src/app/services/events-data.service';

@Component({
  selector: 'app-events-page',
  templateUrl: './events-page.component.html',
  styleUrls: ['./events-page.component.scss']
})
export class EventsPageComponent implements OnInit
{
  title: string = ''
  message: string = ''

  constructor(private eventsDataService: EventsDataService) {}

  ngOnInit(): void {
    this.eventsDataService.getBuckets().subscribe((val) => console.log(val));
  }
  
  storeEvent(){
    console.log(this.title, this.message)
  }
}

import { Component } from '@angular/core';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent {
  goToAdmin(): void{
    window.location.href = 'http://127.0.0.1:8000/django/admin'
  }
}
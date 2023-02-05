import { Component, OnInit } from '@angular/core';
import { AnimationOptions } from 'ngx-lottie';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  size = 'large'
  constructor() { }

  ngOnInit(): void {
    this.display_sessionid();
  }
  options: AnimationOptions = {
    path: '/assets/animations/homelottie.json',
  };


  display_sessionid() {
    console.log("test");
  }

}

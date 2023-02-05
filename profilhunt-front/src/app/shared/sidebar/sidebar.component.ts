import { Component, OnInit } from '@angular/core';
import { NzNotificationService } from 'ng-zorro-antd/notification';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {

  constructor(private notification: NzNotificationService) { }

  ngOnInit(): void {
  }

  notAvailable(data: string): void {
    this.notification.create(
      'error',
      data,
      'This option for searching for someone is not available yet.'
    );
  }

}

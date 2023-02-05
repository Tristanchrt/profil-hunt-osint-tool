import { Component, OnInit } from '@angular/core';
import { NzModalRef } from 'ng-zorro-antd/modal';
import { AnimationOptions } from 'ngx-lottie';

@Component({
  selector: 'app-transaction-modal-failed',
  templateUrl: './transaction-modal-failed.component.html',
  styleUrls: ['./transaction-modal-failed.component.scss']
})
export class TransactionModalFailedComponent implements OnInit {

  ngOnInit(): void {
  }

  constructor(private modal: NzModalRef) { }

  destroyModal(): void {
    this.modal.destroy();
  }

  options: AnimationOptions = {
    path: '/assets/animations/failed.json',
  };
  
}

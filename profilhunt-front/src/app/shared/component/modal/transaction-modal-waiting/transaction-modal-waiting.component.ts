import { NzModalRef } from 'ng-zorro-antd/modal';
import { Component, OnInit } from '@angular/core';
import { AnimationOptions } from 'ngx-lottie';

@Component({
  selector: 'app-transaction-modal-waiting',
  templateUrl: './transaction-modal-waiting.component.html',
  styleUrls: ['./transaction-modal-waiting.component.scss']
})
export class TransactionModalWaitingComponent implements OnInit {


  ngOnInit(): void {
  }

  constructor(private modal: NzModalRef) {}

  destroyModal(): void {
    this.modal.destroy();
  }

  options: AnimationOptions = {
    path: '/assets/animations/loading.json',
  };

}

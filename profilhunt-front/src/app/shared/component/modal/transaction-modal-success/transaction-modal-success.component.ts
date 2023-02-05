import { NzModalRef } from 'ng-zorro-antd/modal';
import { Component, OnInit } from '@angular/core';
import { AnimationOptions } from 'ngx-lottie';

@Component({
  selector: 'app-transaction-modal-success',
  templateUrl: './transaction-modal-success.component.html',
  styleUrls: ['./transaction-modal-success.component.scss']
})
export class TransactionModalSuccessComponent implements OnInit {


  ngOnInit(): void {
  }

  constructor(private modal: NzModalRef) { }

  destroyModal(): void {
    this.modal.destroy();
  }

  options: AnimationOptions = {
    path: '/assets/animations/success.json',
  };

}

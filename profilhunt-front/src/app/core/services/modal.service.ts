import { TransactionModalFailedComponent } from './../../shared/component/modal/transaction-modal-failed/transaction-modal-failed.component';
import { TransactionModalWaitingComponent } from './../../shared/component/modal/transaction-modal-waiting/transaction-modal-waiting.component';
import { Injectable } from '@angular/core';
import { NzModalRef, NzModalService } from 'ng-zorro-antd/modal';
import { TransactionModalSuccessComponent } from 'src/app/shared/component/modal/transaction-modal-success/transaction-modal-success.component';

@Injectable({
  providedIn: 'root'
})
export class ModalService {

  private isVisible: boolean;

  constructor(private modalService: NzModalService) {
    this.isVisible = false;
  }

  transactionSuccess(): void {
    this.modalService.create({
      nzContent: TransactionModalSuccessComponent,
      nzOkDisabled: true,
      nzCancelDisabled: true,
      nzFooter: null,
      nzMaskClosable: false
    });
    this.isVisible = true;
  }
  
  transactionFailed(): void {
    this.modalService.create({
      nzContent: TransactionModalFailedComponent,
      nzOkDisabled: true,
      nzCancelDisabled: true,
      nzFooter: null,
      nzMaskClosable: false
    });
    this.isVisible = true;
  }

  transactionPending(): void {
    this.modalService.create({
      nzContent: TransactionModalWaitingComponent,
      nzOkDisabled: true,
      nzCancelDisabled: true,
      nzFooter: null,
      nzMaskClosable: false
    });
    this.isVisible = true;
  }

  handleOk(): void {
    setTimeout(() => {
      this.isVisible = false;
    }, 1000);
    console.log('Button ok clicked!');
  }

  handleCancel(): void {
    console.log('Button cancel clicked!');
    this.isVisible = false;
  }

  getVisible(): boolean {
    return this.isVisible;
  }

  closeAllModal(): void {
    this.modalService.closeAll();
  }

}

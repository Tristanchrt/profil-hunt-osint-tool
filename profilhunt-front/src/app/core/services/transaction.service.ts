import { ModalService } from './modal.service';
import { Injectable } from '@angular/core';
import { LocalStorageService } from './local-storage.service';
import { ProviderService } from './provider.service';
import {
  Address,
  Account,
  Transaction,
  TransactionVersion
} from '@elrondnetwork/erdjs';
import { SCQueryService } from './sc-query';
import { ITransaction } from '@elrondnetwork/erdjs-web-wallet-provider/out/interface';




@Injectable({
  providedIn: 'root'
})
export class TransactionService {

  constructor(private localStorageService: LocalStorageService, private providerService: ProviderService, private SCQuery: SCQueryService, private modalService: ModalService) { }

  async sendTransaction(transaction: Transaction, isSigned: boolean = false): Promise<any> {
    try {
      let tx = null;
      let account = new Account(new Address(this.localStorageService.get('address')));
      const accountOnNetwork = await ProviderService.proxyProvider.getAccount(new Address(this.localStorageService.get('address')))
      await account.update(accountOnNetwork);
      const provider = await this.providerService.getProvider();
      transaction.setNonce(account.nonce);
      if (!isSigned) {
        tx = await (provider! as any).signTransaction(transaction as ITransaction);
      } else {
        tx = transaction;
      }
      const response = await ProviderService.proxyProvider.sendTransaction(tx);

      this.modalService.transactionPending();
      return await this.checkTransaction(response);
    } catch (e) {
      console.log('error', e);
    }
  };

  async checkTx(transaction: any): Promise<any> {
    const data: any = await this.SCQuery.getTransaction(transaction)
    return data
  }

  async checkTransaction(transaction: string): Promise<any> {

    let resolving = false;
    return new Promise(async (resolve, reject) => {
      while (!resolving) {
        const tx = await this.checkTx(transaction);
        if (tx?.status === "success") {
          resolving = true;
          this.modalService.closeAllModal();
          setTimeout(() => {
            this.modalService.transactionSuccess();
            resolve({ tx: transaction, status: "success" });
          }, 100)
        } else if (tx?.status === "fail" || tx?.status === "invalid") {
          console.log('CC', tx?.status)
          resolving = true;
          this.modalService.closeAllModal();
          setTimeout(() => {
            this.modalService.transactionFailed();
            resolve({ tx: transaction, status: "failed" });
          }, 100)
        } else {
          await this.promiseWaiting(1000);
        }
      }
    }
    )

  }

  async promiseWaiting(time: number) {
    return new Promise(resolve => setTimeout(() =>
      resolve(true)
      , time));
  }

  async decodeUrlTransaction() {
    const provider = await this.providerService.getProvider();
    let plainSignedTransactions = (provider as any).getTransactionsFromWalletUrl();
    let t: Transaction | null = null;
    for (const transaction of plainSignedTransactions) {
      const plainSignedTransactionClone = { ...transaction };
      plainSignedTransactionClone.data = Buffer.from(plainSignedTransactionClone.data).toString("base64");
      t = Transaction.fromPlainObject(plainSignedTransactionClone);
      break;
    }
    return t;
  }



}

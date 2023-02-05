import { Injectable } from '@angular/core';
import { ProviderService } from './provider.service';
import {
  Address,
  ContractFunction,
  SmartContract,
} from '@elrondnetwork/erdjs';
import { environment } from 'src/environments/environment';
import { TransactionService } from './transaction.service';

@Injectable({
  providedIn: 'root'
})
export class ScSearchService {

  constructor(private providerService: ProviderService, private transactionService: TransactionService) { }

  async newSearch(): Promise<any> {
    const contract = new SmartContract({
      address: new Address(environment.scAddress),
    });
    const tx =  contract.call({
      func: new ContractFunction("search"),
      value: "100000000000000",
      args: [],
      gasLimit: 60000000,
      chainID: "D"
    });
    return await this.transactionService.sendTransaction(tx);
  }

}

import { Injectable } from '@nestjs/common';
import { ProxyNetworkProvider } from '@elrondnetwork/erdjs-network-providers';
import {
    Address,
    AddressValue,
    ContractFunction,
    Query,
    Transaction,
    TransactionPayload,
} from '@elrondnetwork/erdjs';
import { catchError, firstValueFrom } from 'rxjs';
import { ConfigService } from '@nestjs/config';
import { loadWallet } from '../scripts/wallet';


@Injectable()
export class SCService {

    constructor(private readonly configService: ConfigService) { }

    public serverAddress: string = this.configService.get('ELROND_URL');
    public proxy: any = new ProxyNetworkProvider(this.serverAddress);
    public SCAddress: string = this.configService.get('SC_ADDRESS');
    public account_wallet: any;

    createQuery(args: Array<any>, func: string): Query {
        const query = new Query({
            address: new Address(this.SCAddress),
            func: new ContractFunction(func),
            args: args
        });
        return query
    }

    async query(args: Array<any>, func: string): Promise<any> {
        const q: any = this.createQuery(args, func);
        const { returnData, returnCode, returnMessage }: any = await this.getProvider().queryContract(q);
        return { returnData, returnCode, returnMessage }
    }

    async removeUserFromPaid(address: string) {
        try {
            
            this.account_wallet = await loadWallet();
            await this.account_wallet.sync(this.proxy);

            let payload = TransactionPayload.contractCall()
                .setFunction(new ContractFunction("remove_user"));

            payload = payload.addArg(new AddressValue(new Address(address)))
            const finalPayload: any = payload.build()

            let tx = new Transaction({
                data: new TransactionPayload(finalPayload),
                gasLimit: 60000000,
                receiver: new Address(this.SCAddress),
                sender: new Address(this.account_wallet.address),
                value: 0,
                chainID: "D"
            });

            tx.setNonce(this.account_wallet.account.nonce);

            await this.account_wallet.signer.sign(tx);
            const response = await this.proxy.sendTransaction(tx);
            console.log("Successfully sent", response);
            return response;
        } catch (e) {
            console.log(`Error removeUserFromPaid ${e}`);
            return;
        }
    }


    getServerAddress(): string {
        return this.serverAddress;
    }
    getSCAddress(): string {
        return this.SCAddress;
    }

    getProvider(): any {
        return this.proxy
    }

}

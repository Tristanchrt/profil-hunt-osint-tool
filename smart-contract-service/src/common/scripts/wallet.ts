const fs = require('fs');
import { Account, Address, AddressValue, BigUIntValue, ContractFunction, TokenIdentifierValue, Transaction, TransactionPayload } from "@elrondnetwork/erdjs/out";
import { UserSecretKey, UserSigner } from "@elrondnetwork/erdjs-walletcore"

interface IAccountBalance { toString(): string; }

interface IAccountOnNetwork {
    nonce: number;
    balance: IAccountBalance;
}

interface IAddress { bech32(): string; }

interface IAccountFetcher {
    getAccount(address: IAddress): Promise<IAccountOnNetwork>;
}

export async function loadWallet(): Promise<Wallet> {
    let keyFileJson = fs.readFileSync("src/wallet/dev-wallet.json", { encoding: "utf8" }).trim();
    let jsonContents = JSON.parse(keyFileJson);
    let pemContents = await readWalletFileContents("src/wallet/dev-wallet.pem");
    let pemKey = UserSecretKey.fromPem(pemContents);
    return new Wallet(
        new Address(jsonContents.address),
        pemKey.hex(),
        jsonContents,
        pemContents);
}

async function readWalletFileContents(path: string): Promise<string> {
    return await fs.promises.readFile(path, { encoding: "utf8" });
}

export class Wallet {
    readonly address: Address;
    readonly secretKeyHex: string;
    readonly secretKey: Buffer;
    readonly signer: UserSigner;
    readonly keyFileObject: any;
    readonly pemFileText: any;
    readonly account: Account | any; 

    constructor(address: Address, secretKeyHex: string, keyFileObject: any, pemFileText: any) {
        this.address = address;
        this.secretKeyHex = secretKeyHex;
        this.secretKey = Buffer.from(secretKeyHex, "hex");
        this.signer = new UserSigner(UserSecretKey.fromString(secretKeyHex));
        this.keyFileObject = keyFileObject;
        this.pemFileText = pemFileText;
        this.account = new Account(this.address);
    }

    async sync(provider: IAccountFetcher) {
        let accountOnNetwork = await provider.getAccount(this.address);
        await this.account.update(accountOnNetwork);
        return this;
    }
}
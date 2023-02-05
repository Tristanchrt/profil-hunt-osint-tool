# ProfilHunt front-end

[![forthebadge](https://forthebadge.com/images/badges/made-with-typescript.svg)](https://forthebadge.com)

## Angular 14, Boostrap 5 & Ant design

- https://angular.io/
- https://getbootstrap.com/
- https://ng.ant.design/
- https://maiar.com/
- https://elrond.com/


## Development server

> Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Build

> Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

> Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

> Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Worker API

- https://developer.mozilla.org/fr/docs/Web/API/Web_Workers_API
- https://angular.io/guide/service-worker-intro

A web worker is available on this website for turning the application into a PWA (Progressive web app)

It is only used for the cache of images, many features are available with this techology however, there are not really usefull for this project

## Elrond API

```ts
// Packages
"@elrondnetwork/erdjs": "^11.1.1",
"@elrondnetwork/erdjs-extension-provider": "^2.0.5",
"@elrondnetwork/erdjs-network-providers": "^1.1.2",
"@elrondnetwork/erdjs-wallet-connect-provider": "^2.0.3",
"@elrondnetwork/erdjs-web-wallet-provider": "^2.1.1",
```

> WARNING: You need the exact same version of the packages

For the communication on the blockchain you'll need use a provider to connect to it. You have 3 methods of connection :
- extension
- qrcode
- webwallet

```ts
// provider.service.ts
async getProvider() {
    if (!ProviderService.current_provider) {
      const walletSession = this.localStorageService.get('walletsession');
      if (walletSession == "extension") {
        ProviderService.current_provider = await this.scExtensionService.getProvider();
      } else if (walletSession == "qrcode") {
        ProviderService.current_provider = await this.scQrcodeService.getProvider();
      } else if (walletSession == "webwallet") {
        ProviderService.current_provider = await this.scWebwalletService.getProvider();
      }else{
        return null;
      }
    }
    return ProviderService.current_provider;
  }

  static async sync() {
    return await ProviderService.proxyProvider.getNetworkConfig()
  }
```

After that you can either create a new transaction or view old research in hunt app.

This part of the code allows yout to create a new transaction and send it to the blockchain.

```ts
// ScSearchService
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

// TransactionService
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
```
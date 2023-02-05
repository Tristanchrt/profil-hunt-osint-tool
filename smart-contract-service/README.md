# Profil hunt smart contract service
[![forthebadge](https://forthebadge.com/images/badges/made-with-rust.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-typescript.svg)](https://forthebadge.com)
## Nestjs and Rust (elrond)

- https://nestjs.com/
- https://elrond.com/
- https://docs.elrond.com/developers/overview/
- https://devnet-explorer.elrond.com/accounts/erd1qv2mdlmma9fqdaxgg7zxl62u4vcjsp6pxx439jglxpdu5kts6rkqtvl2ct
- https://devnet-wallet.elrond.com/unlock/keystore

## Installation and using the applicaiton

> Change /etc/hosts add
```
127.0.0.1 front.eola.local
127.0.0.1 eola.local
```
> Create the newtork docker
```
docker network create ph-test 
```

### How to use

1. Create and configure in the `.env` file  

2. docker-compose up search_service --build

3. Run on port 3000 on address [0.0.0.0](0.0.0.0:3000)

4. `http://ph.local/auth/api` access to the documentation

### Configuration of .env

This is a configuration file that contains all basics necessary configuration for running this service

```
SC_ADDRESS=erd1qqqqqqqqqqqqqpgqt5myzal4ud8yu3f5nayk9dgqvcdr9vzu6rkqjhpusa
ELROND_URL=https://devnet-api.elrond.com
```
# Rust elrond (smart contract)

>A smart contract is a self-executing contract with the terms of the agreement between buyer and seller being directly written into lines of code. The code and the agreements contained therein are stored and replicated on a blockchain network.

>Smart contracts allow for the automation of contract execution and can be used to facilitate, verify, and enforce the negotiation or performance of a contract. They can be implemented in various programming languages, including Rust.

>This smart contract allows you to create a research and add to the list ``userSearch``, and verify if an user is allowed to perform a reseach on the search service. After that the user is removed from the list ``userSearch``, so the user will be able to create an another request again.

> For writiing on the blockchain you need to create a transaction
 
```rust

#[elrond_wasm::contract]
pub trait PingPong {
     /// Necessary configuration when deploying:
    /// `normal_search` - the exact amount that needs to be sent when `ping`-ing.  
    /// `duration_in_seconds` - how much time (in seconds) until `pong` can be called after the initial `ping` call  
    /// `token_id` - Optional. The Token Identifier of the token that is going to be used. Default is "EGLD".
    #[init]
    fn init(&self, min_amount: BigUint, duration_in_seconds: u64, opt_token_id: OptionalValue<EgldOrEsdtTokenIdentifier>) {
        require!(min_amount > 0, "Amount cannot be set to zero");
        self.paymentAmount().set(&min_amount);

        require!(
            duration_in_seconds > 0,
            "Duration in seconds cannot be set to zero"
        );
        self.duration_in_seconds().set(&duration_in_seconds);

        let token_id = match opt_token_id {
            OptionalValue::Some(t) => t,
            OptionalValue::None => EgldOrEsdtTokenIdentifier::egld(),
        };
        self.accepted_payment_token_id().set(&token_id);
    }

    """
    The search function is an endpoint of the contract, which means it can be called 
    by external users. It is marked as payable, which means it can receive 
    a payment in the form of a token transfer
    """
    // endpoints
    #[payable("*")] 
    #[endpoint]
    fn search(&self) {
        let (payment_token, payment_amount) = self.call_value().egld_or_single_fungible_esdt();
        require!(
            payment_token == self.accepted_payment_token_id().get(),
            "Invalid payment token"
        );
        require!(
            payment_amount >= self.paymentAmount().get(),
            "The payment amount must be match your type of research"
        );

        let caller = self.blockchain().get_caller();
        let current_block_timestamp = self.blockchain().get_block_timestamp();

        self.user_search(&caller).set(&current_block_timestamp);
    }
    """
    The remove_user function is also an endpoint, but it is marked with the only_owner attribute, 
    which means it can only be called by the contract's owner. 
    It has a single argument, address, which is the address of a user. 
    The function checks that the user has not paid, and if they have not, it clears 
    their search timestamp from the contract's storage.
    """
    #[only_owner]
    #[endpoint]
    fn remove_user(&self, address: &ManagedAddress) {

        require!(!self.did_user_paid(address), "Not paid yet");
        self.user_search(address).clear();
    }

    """
    The did_user_paid function is a view function, which means it can be called
    to read the contract's storage but cannot modify it. 
    It takes an address as an argument and returns a boolean indicating 
    whether the user at that address has paid.
    """
    // views
    #[view(didUserPaid)]
    fn did_user_paid(&self, address: &ManagedAddress) -> bool {
        !self.user_search(address).is_empty()
    }

    // storage
    #[view(getAcceptedPaymentToken)]
    #[storage_mapper("acceptedPaymentTokenId")]
    fn accepted_payment_token_id(&self) -> SingleValueMapper<EgldOrEsdtTokenIdentifier>;

    #[view(getUserSearch)]
    #[storage_mapper("userSearch")]
    fn user_search(&self, address: &ManagedAddress) -> SingleValueMapper<u64>;

    #[view(getPaymentMethod)]
    #[storage_mapper("paymentMethod")]
    fn paymentAmount(&self) -> SingleValueMapper<BigUint>;

    #[view(getDurationTimestamp)]
    #[storage_mapper("durationInSeconds")]
    fn duration_in_seconds(&self) -> SingleValueMapper<u64>;
}
```

## Installation an deployment

### Step 1: Install erdpy

- https://docs.elrond.com/sdk-and-tools/erdpy/erdpy/

### Step 2: Create a wallet from the devnet

- https://devnet-wallet.elrond.com/unlock/keystore
- And place the .json file provide in the folder smart_contract, after that
create your private key.

```
erdpy --verbose wallet derive ./dev-wallet.pem --mnemonic
```
### Step 3: Give xEGLD on your wallet

- You'll need xEGLD in your wallet to deploy the sc on the devnet

- https://r3d4.fr/faucet?fbclid=IwAR3B2Fxf14O8zwOcNtMz4ufLlIJZb8NBZVMyZx93MxtxvF1H2wsPPQ1rVBo

### Step 3: Build Smart Contract

```
cd smart_contract/ping_pong
erdpy --verbose contract clean
erdpy --verbose contract build
```
### Step 4: Deploy  

- Don't forget the arguments **--arguments 100000000000000 60**

erdpy --verbose contract deploy --pem="../dev-wallet.pem" --gas-limit=200000000 --recall-nonce --bytecode="output/ping-pong.wasm" --proxy="https://devnet-gateway.elrond.com" --chain=D --arguments 100000000000000 60 --send

## Usefull commands

> Deploy the smaet contracts
- erdpy --verbose contract deploy --pem="../dev-wallet.pem" --gas-limit=200000000 --recall-nonce --bytecode="output/ping-pong.wasm" --proxy="https://devnet-gateway.elrond.com" --chain=D --arguments 100000000000000 60 --send

> Query on the sc on the view **didUserPaid**
- erdpy contract query erd1qqqqqqqqqqqqqpgqgefcslhy7kn4y8sfqy99yy6365hv9pcq5znsm5zjaw --proxy="https://devnet-gateway.elrond.com" --function="didUserPaid"
erdpy --verbose contract call 

> Endpoint on the sc on the function **search** which is paypall
- erdpy contract call erd1qqqqqqqqqqqqqpgqt5myzal4ud8yu3f5nayk9dgqvcdr9vzu6rkqjhpusa --pem="../dev-wallet.pem" --gas-limit=200000000 --recall-nonce --proxy="https://devnet-gateway.elrond.com" --chain=D --arguments erd1auyuz6rwv2qwgsmcrzt6ammuc4hqhqa6dgmsk3mjyc7d5jftamwsh3cy7h --send --function="search"

> Function for upgrade your sc don't forget to build the sc before upgrading
- erdpy --verbose contract upgrade erd1qqqqqqqqqqqqqpgqq99fnu2rfc950uungxvpenyy2nhtjzkq6rkqjgf2cx --pem="../dev-wallet.pem" --gas-limit=200000000 --recall-nonce --bytecode="output/sc_adder.wasm" --proxy="https://devnet-gateway.elrond.com" --chain=D --arguments 100000000000000 60 --send


# Nestjs API Elrond


## Installation

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Test

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```


## Architecture DDD (Domain driven design)

This service has been built with the following architecture :

Domain-driven design (DDD) is an approach to software development that focuses on the business domain, or the problem domain, that the software is intended to solve. It is based on the idea that complex systems can be better understood and developed by focusing on the interactions between the various parts of the system, rather than on the individual parts themselves.

In DDD, the business domain is modeled and represented in the code as a set of interconnected objects, known as "entities." These entities are designed to reflect the real-world concepts and relationships that exist within the domain, and they are used to encapsulate the business logic and behavior of the system.

DDD also involves the use of domain-specific languages (DSLs) to express the business rules and constraints in the domain. This helps to create a common understanding of the domain among the developers, as well as to ensure that the code accurately reflects the business requirements. 

## How to communicate with the blockchain elrond

These are packages that allow you to communicate with the elrond blockchain

```
"@elrondnetwork/erdjs": "^11.1.1",
"@elrondnetwork/erdjs-network-providers": "^1.1.2",
"@elrondnetwork/erdjs-walletcore": "^2.1.0",
```

```ts
// Create the connection on the devnet elrond network
new ProxyNetworkProvider(this.serverAddress);

// Create a guery to commmunicate  with the view on your smart contract    
function createQuery(args: Array<any>, func: string): Query {
    const query = new Query({
        address: new Address(this.SCAddress),
        func: new ContractFunction(func),
        args: args
    });
    return query
}
// Run the query with the ProxyNetworkProvider and run the query
async function query(args: Array<any>, func: string): Promise<any> {
    const q: any = this.createQuery(args, func);
    const { returnData, returnCode, returnMessage }: any = await this.getProvider().queryContract(q);
    return { returnData, returnCode, returnMessage }
}
// Fonction that allows you to create a transaction on your SC
async function removeUserFromPaid(address: string) {
    try {
        // load you wallet settings
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

```



import {
    Address,
    Transaction,
    TransactionOptions,
    TransactionPayload,
    TransactionVersion
} from '@elrondnetwork/erdjs';
import { GAS_LIMIT, GAS_PRICE, VERSION, ZERO } from './transaction.interface';
import BigNumber from 'bignumber.js';

export async function transformAndSignTransactions({
    transactions,
}: any): Promise<any> {
    const address: any = JSON.parse(localStorage.getItem('user_info') as any).address as string | Address | Buffer | undefined;
    const nonce = 14;
    return transactions.map((tx: any) => {
        const {
            value,
            receiver,
            data = '',
            chainID,
            version = 1,
            options,
            gasPrice = 1_000_000_000,
            gasLimit = calculateGasLimit(tx.data)
        } = tx;
        let validatedReceiver = receiver;

        const addr = new Address(receiver);
        validatedReceiver = addr.hex();

        return newTransaction({
            value,
            receiver: validatedReceiver,
            data,
            gasPrice,
            gasLimit: Number(gasLimit),
            nonce: Number(nonce.valueOf().toString()),
            sender: new Address(address).hex(),
            chainID: "D",
            version: version,
            options
        });
    });
}


export async function sendTransactions({
    transactions,
    transactionsDisplayInfo,
    redirectAfterSign = false,
    callbackRoute = "",
    signWithoutSending,
    completedTransactionsDelay,
    sessionInformation,
    minGasLimit
}: any): Promise<any> {
    try {
        const transactionsPayload = Array.isArray(transactions)
            ? transactions
            : [transactions];

        const areComplexTransactions = transactionsPayload.every(
            (tx) => Object.getPrototypeOf(tx).toPlainObject != null
        );
        let txToSign = transactionsPayload;
        if (!areComplexTransactions) {
            txToSign = await transformAndSignTransactions({
                transactions: transactionsPayload as any[],
                minGasLimit
            });
            console.log('txToSign 22222', txToSign);
        }

        console.log('txToSign', txToSign);

        return signTransactions({
            transactions: txToSign as any[],
            minGasLimit,
            callbackRoute,
            transactionsDisplayInfo,
            customTransactionInformation: {
                redirectAfterSign,
                completedTransactionsDelay,
                sessionInformation,
                signWithoutSending
            }
        });
    } catch (err) {
        console.error('error signing transaction', err as any);
        return { error: err as any, sessionId: null };
    }
}


function calculateGasLimit(data?: string) {
    const bNconfigGasLimit = 50_000 as any;
    const bNgasPerDataByte = 1_500 as any;
    const bNgasValue = data
        ? bNgasPerDataByte.times(Buffer.from(data).length)
        : 0;
    const bNgasLimit = bNconfigGasLimit.plus(bNgasValue);
    const gasLimit = bNgasLimit.toString(10);
    return gasLimit;
}

export function newTransaction(rawTransaction: any) {
    const { data } = rawTransaction;
    const dataPayload = isStringBase64(data ?? '')
        ? TransactionPayload.fromEncoded(data)
        : new TransactionPayload(data);

    const transaction = new Transaction({
        value: rawTransaction.value.valueOf(),
        data: dataPayload,
        nonce: rawTransaction.nonce.valueOf(),
        receiver: new Address(rawTransaction.receiver),
        sender: new Address(rawTransaction.sender),
        gasLimit: rawTransaction.gasLimit.valueOf() ?? GAS_LIMIT,
        gasPrice: rawTransaction.gasPrice.valueOf() ?? GAS_PRICE,
        chainID: rawTransaction.chainID.valueOf(),
        version: new TransactionVersion(rawTransaction.version ?? VERSION),
        ...(rawTransaction.options
            ? { options: new TransactionOptions(rawTransaction.options) }
            : {})
    });

    transaction.applySignature(
        {
            hex: () => rawTransaction.signature || ''
        },
        new Address(rawTransaction.sender)
    );

    return transaction;
}

export function isStringBase64(string: string) {
    try {
        return Buffer.from(string, 'base64').toString() === atob(string);
    } catch (err) {
        return false;
    }
}

export const stringIsFloat = (amount: string) => {
  if (isNaN(amount as any)) {
    return false;
  }
  if (String(amount).includes('Infinity')) {
    return false;
  }

  // eslint-disable-next-line
  let [wholes, decimals] = amount.split('.');
  if (decimals) {
    while (decimals.charAt(decimals.length - 1) === ZERO) {
      decimals = decimals.slice(0, -1);
    }
  }
  const number = decimals ? [wholes, decimals].join('.') : wholes;
  const bNparsed = new BigNumber(number);
  return bNparsed.toString(10) === number && bNparsed.comparedTo(0) >= 0;
};


export async function signTransactions({
    transactions,
    callbackRoute,
    minGasLimit = GAS_LIMIT,
    customTransactionInformation,
    transactionsDisplayInfo
  }: any): Promise<any> {
    const sessionId = Date.now().toString();
    const accountBalance: any = JSON.parse(localStorage.getItem('user_info') as any).balance as any
    const storeChainId = "D";
  
    const transactionsPayload = Array.isArray(transactions)
      ? transactions
      : [transactions];
    
    const bNbalance = new BigNumber(
      stringIsFloat(accountBalance as any) as any ? accountBalance as any : '0'
    );
    const hasSufficientFunds = bNbalance.minus(10000000).isGreaterThan(0);
  
    if (!hasSufficientFunds) {
      const notificationPayload = {
        type: NotificationTypesEnum.warning,
        iconClassName: "",
        title: 'Insufficient EGLD funds',
        description: 'Current EGLD balance cannot cover the transaction fees.'
      };
      console.log('notificationPayload1', notificationPayload);
      return { error: 'insufficient funds', sessionId: null };
    }
  
    const hasValidChainId = transactionsPayload?.every(
      (tx) => tx.getChainID().valueOf() === storeChainId.valueOf()
    );
    if (!hasValidChainId) {
      const notificationPayload = {
        type: NotificationTypesEnum.warning,
        iconClassName: "",
        title: 'Network change detected',
        description: 'The application tried to change the transaction network'
      };
      console.log('notificationPayload2', notificationPayload);
      return { error: 'Invalid ChainID', sessionId: null };
    }
  
    const signTransactionsPayload = {
      sessionId,
      callbackRoute,
      customTransactionInformation,
      transactions: transactionsPayload.map((tx) => tx.toPlainObject())
    };
    console.log('1',signTransactionsPayload);
    console.log({ sessionId, transactionsDisplayInfo });
    return { sessionId };
  }
  

  export enum NotificationTypesEnum {
    warning = 'warning',
    error = 'error',
    success = 'success'
  }
  

  
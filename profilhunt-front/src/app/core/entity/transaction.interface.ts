interface ScResultType {
    callType: string;
    gasLimit: number;
    gasPrice: number;
    nonce: number;
    prevTxHash: string;
    receiver?: string;
    sender: string;
    value: string;
    data?: string;
    returnMessage?: string;
  }
  
  type TxStatusType = 'pending' | 'notExecuted' | 'success' | 'fail';
  
  export interface TransactionType {
    fee?: string;
    blockHash: string;
    data: string;
    gasLimit: number;
    gasPrice: number;
    gasUsed: string;
    txHash: string;
    miniBlockHash: string;
    nonce: number;
    receiver: string;
    receiverShard: number;
    round: number;
    sender: string;
    senderShard: number;
    signature: string;
    status: TxStatusType;
    timestamp: number;
    value: string;
    scResults?: ScResultType[];
  }
  
  export interface StateType {
    transactions: TransactionType[];
    transactionsFetched: boolean | undefined;
  }

  export const GAS_PRICE_MODIFIER = 0.01;
  export const GAS_PER_DATA_BYTE = 1_500;
  export const GAS_LIMIT = 50_000;
  export const GAS_PRICE = 1_000_000_000;
  export const DECIMALS = 18;
  export const DIGITS = 4;
  export const VERSION = 1;
  
  export const LEDGER_CONTRACT_DATA_ENABLED_VALUE = 1;
  
  export const METACHAIN_SHARD_ID = 4294967295;
  export const ALL_SHARDS_SHARD_ID = 4294967280;
  
  export const DAPP_INIT_ROUTE = '/dapp/init';
  export const WALLET_SIGN_SESSION = 'signSession';
  
  export const LOGOUT_ACTION_NAME = 'logout';
  export const LOGIN_ACTION_NAME = 'login';
  
  export const CANCEL_ACTION_NAME = 'cancelSignTx';
  
  export const REFUNDED_GAS = 'refundedGas';
  
  /**
   * Not Applicable
   * @value N/A
   */
  export const N_A = 'N/A';
  
  export const ZERO = '0';
import { WalletProvider } from '@elrondnetwork/erdjs-web-wallet-provider';
import { ExtensionProvider } from '@elrondnetwork/erdjs-extension-provider';
import { Injectable } from '@angular/core';
import { LocalStorageService } from './local-storage.service';
import { ScExtensionService } from './sc-extension.service';
import { ScQrcodeService } from './sc-qrcode.service';
import { ProxyNetworkProvider } from '@elrondnetwork/erdjs-network-providers/out';
import { environment } from 'src/environments/environment';
import { ScWebwalletService } from './sc-webwallet.service';
import { WalletConnectProvider } from '@elrondnetwork/erdjs-wallet-connect-provider/out';

@Injectable({
  providedIn: 'root'
})
export class ProviderService {

  static current_provider: ExtensionProvider | WalletProvider | WalletConnectProvider;
  static proxyProvider = new ProxyNetworkProvider(environment.gatewayAddress as any, { timeout: 5000 }) as any;

  constructor(private localStorageService: LocalStorageService,
    private scExtensionService: ScExtensionService,
    private scWebwalletService: ScWebwalletService,
    private scQrcodeService: ScQrcodeService) {
    ProviderService.sync();
  }

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
  

}

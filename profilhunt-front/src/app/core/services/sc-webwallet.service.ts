import { Injectable } from '@angular/core';
import { LocalStorageService } from './local-storage.service';
import { WalletProvider } from '@elrondnetwork/erdjs-web-wallet-provider';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ScWebwalletService {

  private webwallet: WalletProvider;

  constructor(private localStorageService: LocalStorageService) {
    this.webwallet = new WalletProvider(environment.devNetAddress);
  }

  async getProvider(): Promise<any> {
    return new Promise((resolve) => resolve(this.webwallet));
  }

  async login() {
    const callbackUrl = encodeURIComponent(environment.url+"/dashboard/profil");
    await this.webwallet.login({ callbackUrl });
    localStorage.setItem('walletsession', "webwallet");
  }

  async logout(){
    this.webwallet.logout();
  }


}

import { Injectable } from '@angular/core';
import {
  WalletConnectProvider
} from '@elrondnetwork/erdjs-wallet-connect-provider/out';
import { LocalStorageService } from './local-storage.service';
import { environment } from 'src/environments/environment';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ScQrcodeService {

  private qrcode: WalletConnectProvider;

  constructor(private localStorageService: LocalStorageService, private router: Router) {
    this.qrcode = new WalletConnectProvider(environment.walletAddress as any, this) as any;
  }

  async login() {
    return await this.qrcode.login();
  }

  async getProvider() : Promise<any> {
    try{
      await this.init();
    }catch(e){ }
    return this.qrcode;
  }

  async onClientLogout() {
    this.localStorageService.clear("address");
    this.localStorageService.clear("walletsession");
    this.qrcode.logout();
  }

  async onClientLogin() {
    if (this.qrcode) {
      const address = await this.qrcode.getAddress();
      this.localStorageService.set("address", address);
      this.localStorageService.set('walletsession', "qrcode");
      this.router.navigate(['dashboard/first-last-name']);
    }
  }

  async init() {
    await this.qrcode.init();
  }

  async logout() {
    this.onClientLogout();
  }

}

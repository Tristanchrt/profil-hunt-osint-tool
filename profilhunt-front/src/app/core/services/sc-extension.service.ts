import { LocalStorageService } from './local-storage.service';
import { Injectable } from '@angular/core';
import { ExtensionProvider } from '@elrondnetwork/erdjs-extension-provider';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ScExtensionService {

  private extension: ExtensionProvider;

  constructor(private localStorageService: LocalStorageService, private router: Router) {
    this.extension = ExtensionProvider.getInstance()
    let address = this.localStorageService.get("address");
    if(address){
      this.extension.setAddress(address);
    }
  }
  
  async login() {
    await this.extension.login();
    const { address } = this.extension.account;
    if (!address) {
      console.warn('Login cancelled.');
      return;
    }
    this.localStorageService.set("address", address);
    this.localStorageService.set('walletsession', "extension");
    this.router.navigate(['dashboard/first-last-name']);
  }

  async getProvider(): Promise<any> {
    return new Promise((resolve) => resolve(this.extension));
  }

  async init() {
    await this.extension.init();
  }

  async logout() {
    this.extension.logout();
  }

}

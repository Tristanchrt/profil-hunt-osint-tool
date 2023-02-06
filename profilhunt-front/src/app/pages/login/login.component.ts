import { ScQrcodeService } from './../../core/services/sc-qrcode.service';
import { ScExtensionService } from './../../core/services/sc-extension.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ScWebwalletService } from 'src/app/core/services/sc-webwallet.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {


  constructor(private scExtension: ScExtensionService, private scQrcodeService: ScQrcodeService, private scWebwalletService: ScWebwalletService) {}

  public myAngularxQrCode: string = "";

  async ngOnInit(): Promise<void> {
    (window as any).global = window;
    await this.scQrcodeService.init()
    const uri = await this.scQrcodeService.login()
    this.myAngularxQrCode = uri;
  }

  async authExtension() {
    this.scExtension.init();
    this.scExtension.login(); 
  }

  async authWebWallet() {
    this.scWebwalletService.login();
  }

}

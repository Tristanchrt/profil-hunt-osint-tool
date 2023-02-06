import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from 'src/app/core/services/local-storage.service';
import { Router } from "@angular/router"
import { ScWebwalletService } from 'src/app/core/services/sc-webwallet.service';
import { ProviderService } from 'src/app/core/services/provider.service';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(private localStorageService: LocalStorageService, private router: Router, private providerService: ProviderService) { }

  ngOnInit(): void {
  }

  isLogin(): boolean {
    return this.localStorageService.get('address');
  }

  
  async logout(): Promise<any> {
    (await this.providerService.getProvider())?.logout();
    this.localStorageService.cleaAll();
    this.router.navigate(['/']);
    setTimeout(() => {
      window.location.reload();
    }, 200)
  }

}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class SCQueryService {

  constructor(private http: HttpClient, private router: Router, private localStorageService: LocalStorageService) { }

  async getTimeToPong(address: string): Promise<any> {
    try {
      const data: any = await firstValueFrom(this.http.get(`${environment.apiUrl}/search/account/${address}`));
      return data.body;
    } catch (e) {
      console.log('Error: getTimeToPong' + e)
      return null;
    }
  }

  async getAccountInfo(address: string): Promise<any> {
    try {
      const data: any = await firstValueFrom(this.http.get(`${environment.devNetAddress}/accounts/${address}`));
      return data;
    } catch (e) {
      console.log('Error: getAccountInfo' + e)
      return null;
    }
  }
  
  async getTransaction(transaction: string): Promise<any> {
    try {
      const data: any = await firstValueFrom(this.http.get(`${environment.devNetApi}/transactions/${transaction.toString()}`));
      return data;
    } catch (e) {
      console.log('Error: getTransaction' + e)
      return null;
    }
  }
  
  getAddress(): string {
    return this.localStorageService.get('address');
  }

  getUserInfo(): any {
    try {
      return JSON.parse(this.localStorageService.get('user_info'))
    } catch (e) {
      return e
    }
  }

  async clientConnect(address: string): Promise<void> { 
    const data = await this.getAccountInfo(address);
    this.localStorageService.set('user_info', JSON.stringify(data));
    this.router.navigate(['/dashboard'])
  }

}

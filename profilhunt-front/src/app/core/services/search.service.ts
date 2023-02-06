import { HttpClient } from '@angular/common/http';
import { Injectable, NgZone } from '@angular/core';
import { firstValueFrom, last } from 'rxjs';
import { environment } from 'src/environments/environment';
import { LogService } from './log.service';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient, private loggerService: LogService) { }

  async postsearchFirstLastName(firstName: any, lastName: any, paramsValue: any) {
    try {
      if(paramsValue && paramsValue.length > 0) { 
        paramsValue = paramsValue ? paramsValue.split(",") : []
      }else{
        paramsValue = []
      }
      let user_address = localStorage.getItem('address');
      const data = {
        "first_name": firstName,
        "last_name": lastName,
        "params": paramsValue,
        "user_address": user_address
      }
      const httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
      return await firstValueFrom(this.http.post(`${environment.apiUrl}/search`, data ));
    } catch (error) {
      this.loggerService.log(error)
      return false;
    }
  }

  async getAllsearchFirstLastName(indexPag: any) {
    try {
      return await firstValueFrom(this.http.get(`${environment.apiUrl}/search/${indexPag}`).pipe());
    } catch (error) {
      this.loggerService.log(error)
      return false;
    }
  }

}

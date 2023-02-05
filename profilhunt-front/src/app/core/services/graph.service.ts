import { HttpClient } from '@angular/common/http';
import { Injectable, NgZone } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';
import { LogService } from './log.service';

@Injectable({
  providedIn: 'root'
})
export class GraphService {

  constructor(private http: HttpClient, private loggerService: LogService) { }


  async getGraphById(id: string) {
    try {
      return await firstValueFrom(this.http.get(`${environment.apiUrl}/graph/`+id));
    } catch (error) {
      this.loggerService.log(error)
      return false;
    }
  }

}

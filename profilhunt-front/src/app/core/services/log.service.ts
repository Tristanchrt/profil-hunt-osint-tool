import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor() { }

  log(text: any){
    if (!environment.production) {
      console.log(text)
    }
  }

}

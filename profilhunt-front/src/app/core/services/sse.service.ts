import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class SseService {

  constructor() { }
  
  private subj = new BehaviorSubject({});
  private envS: EventSource;

  returnAsObservable(): Observable<any> {
    return this.subj.asObservable();
  }

  getEvents(path: string): void {
    let subject = this.subj;
    this.envS = new EventSource(`${environment.apiUrl}${path}`);

    this.envS.onopen = () => {
      console.log("Connected to stream", path);
    }

    this.envS.addEventListener('new_message', event => {
      // console.log('Event received : ' + event.data);
      subject.next(event["data"]);
    })
    this.envS.onerror = function (e) {
      console.log(e);
      if (this.readyState == 0) {
        console.log("Reconnecting…");
      }
    }
  }

  stopExchangeUpdates() {
    this.envS.close();
  }

}



import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  constructor() { }

  public set(key: string, value: any): void { 
    localStorage.setItem(key, value);
  }

  public get(key: string): any { 
      return localStorage.getItem(key);
  }

  public cleaAll(): void { 
    localStorage.clear();
  }

  public clear(key: string): void { 
    localStorage.removeItem(key);
  }

  public getALl(key: string): any { 
    return { ...localStorage }
  }

}

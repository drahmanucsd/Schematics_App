import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  private baseUrl = 'http://127.0.0.1:8000/api/v1/Data/';

  constructor(private http: HttpClient) { }

  search(params: any): Observable<any> {
    return this.http.get(`${this.baseUrl}`, { params });
  }
}

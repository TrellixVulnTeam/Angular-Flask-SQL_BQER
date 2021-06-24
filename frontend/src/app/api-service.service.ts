import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { API_URL } from '../environments/environment';
import { Observable } from 'rxjs'

@Injectable()
export class ApiService {

  apiUrl : string

  constructor(private http: HttpClient) {
    if(API_URL.charAt(API_URL.length - 1) == '/')
      this.apiUrl = API_URL
    else
      this.apiUrl = API_URL + '/'
   }

  private httpGet(url : string): Observable<any>{
    return this.http.get(this.apiUrl + url);
  }

  private httpDelete(url : string) : Observable<any>{
    return this.http.delete(this.apiUrl + url)
  }

  private httpPost(url : string, body : any) : Observable<any>{
    throw this.http.post(this.apiUrl + url, body)
  }

  private httpPut(url : string, body : any) : Observable<any>{
    throw this.http.put(this.apiUrl + url, body)
  }

  //GET: index
  public getIndex() : Observable<any> {
    return this.httpGet("");
  }

}

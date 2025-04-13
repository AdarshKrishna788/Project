import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { loginData, signupData } from '../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:5000/api/auth';

  constructor(private http: HttpClient) {}

  signup(userData: signupData): Observable<signupData> {
    return this.http.post<signupData>(`${this.apiUrl}/signup`, userData);
  }

  login(userData: loginData): Observable<any> {
    return this.http.post<loginData>(`${this.apiUrl}/login`, userData);
  }

  logout() {
    this.http.post(`${this.apiUrl}/logout`, "").subscribe({
      next:(res)=>{
        console.log("logout res",res)
        localStorage.removeItem('user');
        console.log("Logout successfully")
      },
      error:(err)=>{console.log("Error in logout",err)}
    });
  }

  getCurrentUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }

  getModelResponse(formData: { [key: string]: number }): Observable<any> {
      return this.http.post<any>("http://localhost:9696/predict", formData);
    }
  
  
}

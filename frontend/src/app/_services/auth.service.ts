import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Login } from '../_models/login';
import { Register } from '../_models/register';
import { TokenService } from './token-storage.service';

const baseUrl: string = environment.baseUrl;

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient, private tokenService: TokenService, private router: Router) { }

  isLoggedIn(): boolean {
    return this.tokenService.getToken() !== null;
  }

  login(login: Login): Observable<any> {
    return this.http.post(baseUrl + '/login', login);
  }

  register(register: Register): Observable<any> {
    return this.http.post(baseUrl + '/register', register);
  }

  logout(): void {
    window.localStorage.clear();
    this.router.navigate(['']);
  }
}

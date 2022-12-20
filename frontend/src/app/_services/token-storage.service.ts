import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Claims } from '../_models/claims';

const TOKEN_KEY = 'auth-token';

@Injectable({
  providedIn: 'root'
})
export class TokenService {

  constructor(private jwtHelper: JwtHelperService) { }

  public saveToken(token: string): void {
    window.localStorage.removeItem(TOKEN_KEY);
    window.localStorage.setItem(TOKEN_KEY, token);
  }

  public getToken(): string | null {
    return window.localStorage.getItem(TOKEN_KEY);
  }

  public getTokenExpirationDate(): Date | null {
    return this.jwtHelper.getTokenExpirationDate();
  }

  public isTokenExpired(): boolean {
    return this.jwtHelper.isTokenExpired();
  }

  public decodeToken(): Claims {
    return this.jwtHelper.decodeToken(this.getToken() ?? '').sub;
  }
}

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Login } from 'src/app/_models/login';
import { AuthService } from 'src/app/_services/auth.service';
import { TokenService } from 'src/app/_services/token-storage.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  login: Login = {
    email: '',
    password: ''
  };

  constructor(private router: Router, private authService: AuthService, private tokenService: TokenService) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.authService.login(this.login).subscribe(res => {
      console.log(res);
      if (res.token) {
        this.tokenService.saveToken(res.token);
        this.router.navigate(['/dashboard']);
      }
    },
      err => {
        console.error(err.error);
      });
  }

}

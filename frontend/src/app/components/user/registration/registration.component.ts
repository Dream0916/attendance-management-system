import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { Register } from 'src/app/_models/register';
import { AuthService } from 'src/app/_services/auth.service';
import { ToasterService } from 'src/app/_services/toaster.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  @ViewChild('registerForm', { static: false }) registerForm!: NgForm;

  confirmPasswordError = false;
  register: Register = {
    email: '',
    password: '',
    confirmPassword: ''
  }

  constructor(private authService: AuthService, private toaster: ToasterService) { }

  ngOnInit(): void {
  }

  onPasswordChange(event: any): void {
    this.confirmPasswordError = this.register.password !== this.register.confirmPassword;
  }

  onSubmit(): void {
    if (this.register.password !== this.register.confirmPassword) {
      this.confirmPasswordError = true;
      return;
    }

    this.authService.register(this.register).subscribe(res => {
      this.toaster.success('Registered', 'Your registration is done successfully.');
      this.registerForm.resetForm();
    },
      err => {
        console.error(err.error);
      });
  }

}

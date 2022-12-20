import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class ToasterService {

  constructor(private toastr: ToastrService) { }

  success(title: string, message: string): void {
    this.toastr.success(
      `<span data-notify="icon" class="nc-icon nc-bell-55"></span><b>${title}</b><br><span data-notify="message">${message}</span>`,
      "",
      {
        timeOut: 4000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-success alert-with-icon",
        positionClass: "toast-top-right"
      });
  }

  info(title: string, message: string): void {
    this.toastr.success(
      `<span data-notify="icon" class="nc-icon nc-bell-55"></span><b>${title}</b><br><span data-notify="message">${message}</span>`,
      "",
      {
        timeOut: 4000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-info alert-with-icon",
        positionClass: "toast-top-right"
      });
  }

  warning(title: string, message: string): void {
    this.toastr.success(
      `<span data-notify="icon" class="nc-icon nc-bell-55"></span><b>${title}</b><br><span data-notify="message">${message}</span>`,
      "",
      {
        timeOut: 4000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-warning alert-with-icon",
        positionClass: "toast-top-right"
      });
  }

  error(title: string, message: string): void {
    this.toastr.success(
      `<span data-notify="icon" class="nc-icon nc-bell-55"></span><b>${title}</b><br><span data-notify="message">${message}</span>`,
      "",
      {
        timeOut: 4000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-danger alert-with-icon",
        positionClass: "toast-top-right"
      });
  }
}

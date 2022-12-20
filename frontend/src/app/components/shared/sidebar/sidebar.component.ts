import { Component, OnInit } from '@angular/core';


export interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}

export const ROUTES: RouteInfo[] = [
    { path: '/dashboard', title: 'Dashboard', icon: 'nc-bank', class: '' },
    { path: '/department', title: 'Masters', icon: 'nc-tile-56', class: '' },
    { path: '/employee', title: 'Employee', icon: 'nc-circle-10', class: '' },
    // { path: '/maps', title: 'Maps', icon: 'nc-pin-3', class: '' },
    // { path: '/notifications', title: 'Notifications', icon: 'nc-bell-55', class: '' },
    // { path: '/table', title: 'Table List', icon: 'nc-tile-56', class: '' },
    // { path: '/typography', title: 'Typography', icon: 'nc-caps-small', class: '' },
    // { path: '/register', title: 'Register', icon: 'nc-caps-small', class: '' },
    // { path: '/upgrade', title: 'Upgrade to PRO', icon: 'nc-spaceship', class: 'active-pro' },
];

@Component({
    selector: 'sidebar-cmp',
    templateUrl: 'sidebar.component.html',
})

export class SidebarComponent implements OnInit {
    public menuItems: RouteInfo[] = [];
    ngOnInit() {
        this.menuItems = ROUTES.filter(menuItem => menuItem);
    }
}

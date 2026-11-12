import { Routes } from '@angular/router';
import { FormRegisterPage } from './pages/form-register-page/form-register-page';
import { PageNotFound } from './pages/page-not-found/page-not-found';

export const routes: Routes = [
    { path: '', pathMatch: 'full', component: FormRegisterPage },
    { path: '**', component: PageNotFound }
];

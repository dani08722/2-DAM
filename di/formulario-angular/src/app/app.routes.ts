import { Routes } from '@angular/router';
import { Formulario } from './components/formulario/formulario';
import { PageNotFound } from './pages/page-not-found/page-not-found';

export const routes: Routes = [
    {path: 'formulario', component: Formulario},
    {path: '', pathMatch: 'full', redirectTo: '/formulario'},
    {path:'**', component: PageNotFound}
];

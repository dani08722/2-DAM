import { Routes } from '@angular/router';
import { CustomProgressBarComponent } from './components/custom-progess-bar-component/custom-progess-bar-component';
import { PageNotFound } from './pages/page-not-found/page-not-found';

export const routes: Routes = [
    {path: 'barra-progreso', component: CustomProgressBarComponent},
    {path: '', pathMatch: 'full', redirectTo: '/barra-progreso'},
    {path:'**', component: PageNotFound}
];

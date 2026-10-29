import { Routes } from '@angular/router';
<<<<<<< HEAD
import { FormularioComponent } from './components/formulario-component/formulario-component';
import { NotFoundPages } from './pages/not-found-pages/not-found-pages';

export const routes: Routes = [
    {path:'formulario', component:FormularioComponent},
    {path:'', pathMatch: 'full', redirectTo: '/formulario'},
    {path:'**', component:NotFoundPages}
=======
import { Formulario } from './components/formulario/formulario';
import { PageNotFound } from './pages/page-not-found/page-not-found';

export const routes: Routes = [
    {path: 'formulario', component: Formulario},
    {path: '', pathMatch: 'full', redirectTo: '/formulario'},
    {path:'**', component: PageNotFound}
>>>>>>> 489f18378362a303a27d9043d4d0df54611ad4ca
];

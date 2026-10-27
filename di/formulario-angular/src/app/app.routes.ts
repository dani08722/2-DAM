import { Routes } from '@angular/router';
import { FormularioComponent } from './components/formulario-component/formulario-component';
import { NotFoundPages } from './pages/not-found-pages/not-found-pages';

export const routes: Routes = [
    {path:'formulario', component:FormularioComponent},
    {path:'', pathMatch: 'full', redirectTo: '/formulario'},
    {path:'**', component:NotFoundPages}
];

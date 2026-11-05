import { Routes } from '@angular/router';
import { PeopleListComponent } from './components/people-list-component/people-list-component';
import { PageNotFound } from './components/page-not-found/page-not-found';

export const routes: Routes = [
    {path: 'people-list', component: PeopleListComponent},
    {path: '', pathMatch:'full', redirectTo: '/people-list'},
    {path: '**', component: PageNotFound}
];

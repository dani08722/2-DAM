import { Routes } from '@angular/router';
import { RickymortyListComponent } from './components/rickymorty-list-component/rickymorty-list-component';
import { PageNotFound } from './pages/page-not-found/page-not-found';
import { EpisodeListComponent } from './components/episode-list-component/episode-list-component';

export const routes: Routes = [
    {path: 'rickmorty-list', component: RickymortyListComponent},
    {path: 'episode-list', component: EpisodeListComponent},
    {path: '', pathMatch: 'full', redirectTo: '/rickmorty-list'},
    {path: '**', component: PageNotFound}
];

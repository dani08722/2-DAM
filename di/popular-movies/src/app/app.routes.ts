import { Routes } from '@angular/router';
import { PopularMoviesPage } from './pages/popular-movies-page/popular-movies-page';

export const routes: Routes = [
  { path: '', redirectTo: 'popular', pathMatch: 'full' },
  { path: 'popular', component: PopularMoviesPage, title: 'Películas populares | Popular Movies' },
  { path: '**', redirectTo: 'popular' },
];

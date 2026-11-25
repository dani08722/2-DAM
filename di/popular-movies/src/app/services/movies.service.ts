import { HttpClient, HttpParams } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { PopularMoviesResponse } from '../models/popular-movies-response.interface';

@Injectable({ providedIn: 'root' })
export class MoviesService {
  private readonly http = inject(HttpClient);
  private readonly popularMoviesUrl = environment.tmdbBaseUrl + '/movie/popular';

  getPopularMovies(page = 1): Observable<PopularMoviesResponse> {
    const params = new HttpParams()
      .set('api_key', environment.tmdbApiKey)
      .set('language', 'es-ES')
      .set('page', page);

    return this.http.get<PopularMoviesResponse>(this.popularMoviesUrl, { params });
  }
}

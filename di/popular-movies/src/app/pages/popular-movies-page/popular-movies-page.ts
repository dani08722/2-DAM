import { Component, DestroyRef, inject } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { Movie } from '../../models/popular-movies-response.interface';
import { MoviesService } from '../../services/movies.service';

@Component({
  selector: 'app-popular-movies-page',
  imports: [RouterLink, RouterLinkActive],
  templateUrl: './popular-movies-page.html',
  styleUrl: './popular-movies-page.css',
})
export class PopularMoviesPage {
  private readonly moviesService = inject(MoviesService);
  private readonly destroyRef = inject(DestroyRef);

  protected movies: Movie[] = [];
  protected currentPage = 1;
  protected totalPages = 1;
  protected totalResults = 0;
  protected loading = true;
  protected errorMessage = '';

  protected get featuredMovie(): Movie | null {
    return this.movies[0] ?? null;
  }

  protected get supportingMovies(): Movie[] {
    return this.movies.slice(1);
  }

  constructor() {
    this.loadPopularMovies();
  }

  protected loadPopularMovies(page = this.currentPage): void {
    this.loading = true;
    this.errorMessage = '';

    this.moviesService.getPopularMovies(page)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: (response) => {
          this.movies = response.results ?? [];
          this.currentPage = response.page;
          this.totalPages = Math.max(1, Math.min(response.total_pages, 500));
          this.totalResults = response.total_results;
          this.loading = false;
        },
        error: () => {
          this.loading = false;
          this.errorMessage = 'No se pudieron cargar las películas. Comprueba la conexión y la configuración de TMDB.';
        },
      });
  }

  protected posterUrl(path: string): string {
    return 'https://image.tmdb.org/t/p/w500' + path;
  }

  protected backdropStyle(path: string | null): string {
    return path ? 'url("https://image.tmdb.org/t/p/w1280' + path + '")' : 'none';
  }

  protected year(releaseDate: string): string {
    const year = releaseDate ? new Date(releaseDate + 'T00:00:00').getFullYear() : NaN;
    return Number.isNaN(year) ? 'Fecha por confirmar' : String(year);
  }

  protected rating(value: number): string {
    return value > 0 ? value.toFixed(1) : '—';
  }
}

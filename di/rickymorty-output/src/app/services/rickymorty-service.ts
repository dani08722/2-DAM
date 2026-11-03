import { HttpClient } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { Observable } from 'rxjs';
import { RickymortyListResponse } from '../interfaces/rickymorty-list-response';
import { RickymortyDetailResponse } from '../interfaces/rickymorty-detail-response';

@Service()
export class RickymortyService {
    http = inject(HttpClient);

    getAll(): Observable<RickymortyListResponse> {
        return this.http.get<RickymortyListResponse>('https://rickandmortyapi.com/api/character');
    }

    getOne(id: number): Observable<RickymortyDetailResponse> {
        return this.http.get<RickymortyDetailResponse>(`https://rickandmortyapi.com/api/character/${id}`);
    }
}
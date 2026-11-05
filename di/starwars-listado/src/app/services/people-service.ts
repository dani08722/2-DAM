import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { PeopleListResponse } from '../interfaces/people-list-response';
import { Observable } from 'rxjs';
import { PeopleDetailResponse } from '../interfaces/people-detail-response';

@Injectable({ providedIn: 'root' })
export class PeopleService {
    http= inject(HttpClient)

    getAll():Observable<PeopleListResponse>{
        return this.http.get<PeopleListResponse>('https://swapi.dev/api/people');
    }

    getOne(id:number):Observable<PeopleDetailResponse>{
        return this.http.get<PeopleDetailResponse>(`https://swapi.dev/api/people/${id}/`)
    }
}

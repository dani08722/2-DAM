import { Component, inject, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { PeopleDetailResponse } from '../../interfaces/people-detail-response';

@Component({
  imports: [],
  selector: 'app-people-modal',
  styleUrl: './people-modal.css',
  templateUrl: './people-modal.html',
})
export class PeopleModal {
  activeModal=inject(NgbActiveModal);
  @Input() peopleDetail: PeopleDetailResponse | undefined;
}

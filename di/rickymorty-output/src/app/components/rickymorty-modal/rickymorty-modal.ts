import { Component, inject, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { RickymortyDetailResponse } from '../../interfaces/rickymorty-detail-response';

@Component({
  imports: [],
  selector: 'app-rickymorty-modal',
  styleUrl: './rickymorty-modal.css',
  templateUrl: './rickymorty-modal.html',
})
export class RickymortyModal {
  activeModal = inject(NgbActiveModal);
  @Input() characterDetail: RickymortyDetailResponse | undefined;
}

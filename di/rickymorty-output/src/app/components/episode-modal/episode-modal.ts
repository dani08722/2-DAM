import { Component, inject, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { EpisodeDetailResponse } from '../../interfaces/episode-detail-response';

@Component({
  imports: [],
  selector: 'app-episode-modal',
  styleUrl: './episode-modal.css',
  templateUrl: './episode-modal.html',
})
export class EpisodeModal {
  activeModal=inject(NgbActiveModal);
  @Input() episodeDetail: EpisodeDetailResponse | undefined;
}

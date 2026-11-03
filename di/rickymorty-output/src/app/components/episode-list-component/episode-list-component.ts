import { Component, inject, OnInit, signal } from '@angular/core';
import { EpisodeService } from '../../services/episode-service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { EpisodeModal } from '../episode-modal/episode-modal';
import { Episode } from '../../interfaces/episode-list-response';
import { EpisodeItemComponent } from '../episode-item-component/episode-item-component';

@Component({
  imports: [ EpisodeItemComponent],
  selector: 'app-episode-list-component',
  styleUrl: './episode-list-component.css',
  templateUrl: './episode-list-component.html',
})
export class EpisodeListComponent implements OnInit{
  
  episodeService = inject(EpisodeService);
  episodeList = signal<Episode[]>([]);
  private modalService = inject(NgbModal);

  ngOnInit(): void {
    this.episodeService.getAllEpisodes().subscribe(resp => {
      this.episodeList.set(resp.results);
    });
  }

  openPokemonModal(id: number){
    this.episodeService.getOneEpisode(id).subscribe(resp => {
      const modalRef = this.modalService.open(EpisodeModal);
      modalRef.componentInstance.episodeDetail=resp;
    });
  }
}

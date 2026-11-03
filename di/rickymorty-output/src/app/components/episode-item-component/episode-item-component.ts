import { Component, input, output } from '@angular/core';
import { Episode } from '../../interfaces/episode-list-response';

@Component({
  imports: [],
  selector: 'app-episode-item-component',
  styleUrl: './episode-item-component.css',
  templateUrl: './episode-item-component.html',
})
export class EpisodeItemComponent {
  episode = input<Episode>();

  episodeClicked = output <string> ();
  id : string = '';

  getEpisodeId(){
    this.id = this.episode()?.url.split("/")[5]!;
    return this.id;
  }

  emitCharacterClicked(){
    const id = this.getEpisodeId();
    this.episodeClicked.emit(id);
  }
}

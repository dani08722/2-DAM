import { Component, input, output } from '@angular/core';
import { Character } from '../../interfaces/rickymorty-list-response';

@Component({
  imports: [],
  selector: 'app-rickymorty-item-component',
  styleUrl: './rickymorty-item-component.css',
  templateUrl: './rickymorty-item-component.html',
})
export class RickymortyItemComponent {

  character=input<Character>();

  characterClicked=output<string>();
  id:string='';

  getCharacterId() {
    this.id = this.character()?.url.split("/")[5]!;
    return this.id;
  }

  emitCharacterClicked() {
    const id = this.getCharacterId();
    this.characterClicked.emit(id);
  }

}

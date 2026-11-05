import { Component, input, output } from '@angular/core';
import { Characters } from '../../interfaces/people-list-response';

@Component({
  imports: [],
  selector: 'app-people-item-component',
  styleUrl: './people-item-component.css',
  templateUrl: './people-item-component.html',
})
export class PeopleItemComponent {
  character= input<Characters>();

  characterClicked = output<number>();
  id = 0;

  getCharacterId(){
    this.id=Number(this.character()?.url.split("/")[5]);
    return this.id
  }

  emitCharacterClicked(){
    const id = this.getCharacterId();
    this.characterClicked.emit(id);
  }
}

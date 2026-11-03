import { Component, inject, signal } from '@angular/core';
import { RickymortyService } from '../../services/rickymorty-service';
import { Character } from '../../interfaces/rickymorty-list-response';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RickymortyModal } from '../rickymorty-modal/rickymorty-modal';
import { RickymortyItemComponent } from '../rickymorty-item-component/rickymorty-item-component';

@Component({
  imports: [RickymortyItemComponent],
  selector: 'app-rickymorty-list-component',
  styleUrl: './rickymorty-list-component.css',
  templateUrl: './rickymorty-list-component.html',
})
export class RickymortyListComponent{
  rickymortyService = inject(RickymortyService);
  characterList = signal<Character[]>([]);
  private modalService = inject(NgbModal);

    ngOnInit(): void {
   this.rickymortyService.getAll().subscribe(resp => {
      this.characterList.set(resp.results);
    });
  }

  // STEP10: en este método voy a recibir el ID del Pokémon, que me ha enviado por el output el componente Hijo
  // y voy a abrir un modal con la información de ese Pokémon
  openPokemonModal(id: number) {
    // definimos la llamada al servicio RickymortyService, que me devuelve la información de un Pokémon a partir de su ID
    this.rickymortyService.getOne(id).subscribe(resp => {

      // STEP12: abro el modal que está declarado en el componente RickymortyModal y le paso la información del detalle que he recibido de la API
          const modalRef = this.modalService.open(RickymortyModal);
		      modalRef.componentInstance.characterDetail = resp;
    });

  }
}

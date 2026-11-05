import { Component, inject, OnInit, signal } from '@angular/core';
import { PeopleService } from '../../services/people-service';
import { Characters } from '../../interfaces/people-list-response';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { PeopleModal } from '../people-modal/people-modal';
import { PeopleItemComponent } from '../people-item-component/people-item-component';

@Component({
  imports: [PeopleItemComponent],
  selector: 'app-people-list-component',
  styleUrl: './people-list-component.css',
  templateUrl: './people-list-component.html',
})
export class PeopleListComponent implements OnInit{
  
  peopleService = inject(PeopleService)
  peopleList= signal<Characters[]>([]);
  private modalService = inject(NgbModal);

  ngOnInit(): void {
    this.peopleService.getAll().subscribe(resp =>{
      this.peopleList.set(resp.results);
    })
  }

  openCharacterModal(id: number){
    this.peopleService.getOne(id).subscribe(resp => {
      const modalRef = this.modalService.open(PeopleModal);
      modalRef.componentInstance.peopleDetail=resp;
    });
  }


}

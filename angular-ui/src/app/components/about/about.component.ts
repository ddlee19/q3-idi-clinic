import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ModalService } from '../../services/modal.service';

/** The component for the "About" modal window. */
@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  /** 
   * A reference to the modal Observable indicating whether the modal should be open or closed. 
   */
  display$: Observable<'open' | 'close'>;

  /**
   * The class constructor
   * 
   * @param modalService: an injected instance of the modal service
   */
  constructor(private modalService: ModalService) {}

  /** Subscribes to the modal service when the component is initialized. */
  ngOnInit() {
    this.display$ = this.modalService.watch();
  }

  /** Calls the modal service to close the modal window. */
  close() {
    this.modalService.close();
  }
}

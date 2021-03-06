import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ModalService } from '../../services/modal.service';

/** A component for the main navigation bar. */
@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  /** 
   * A boolean indicating whether the navigation bar should be displayed.
   * Defaults to true.
   */
  @Input() showNav: boolean = true;

  /** Emits the name of a filter when that filter is opened */
  @Output() openFilterEvent = new EventEmitter<string>();

  /**
  * Emits an event broadcasting that the user has opened the given filter.
  */
  openFilter(value: string) {
    this.openFilterEvent.emit(value);
  }

  /* Calls the modal service to launch the "About" modal window. */
  launchModal() {
    this.modalService.open();
  }
  
  /**
   * The class constructor
   * 
   * @param modalService: An injected instance of the ModalService
   */
  constructor(private modalService: ModalService) { }

  /** 
   * A callback method that is invoked immediately after Angular has completed
   * initialization of a component's view. It is invoked only once when the
   * view is instantiated. (See "https://angular.io/api/core/AfterViewInit".)
   */
  ngOnInit(): void {
  }
}

import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { AboutComponent } from '../about/about.component';
declare var $: any 

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  @Input() showNav: boolean = true;

  @Output() openFilterEvent = new EventEmitter<string>();

  openFilter(value: string) {
    this.openFilterEvent.emit(value);
  }

  launchModal() {
    // Sample code from 'https://semantic-ui.com/modules/modal.html#/definition'
    $('.ui.modal').modal('show');
  }
  constructor() { }

  ngOnInit(): void {
  }
}

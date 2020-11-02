import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

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

  constructor() { }

  ngOnInit(): void {
  }
}

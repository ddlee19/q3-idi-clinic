import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  launchModal() {
    // Sample code from 'https://semantic-ui.com/modules/modal.html#/definition'
    //$('.ui.modal').modal('show');
  }

  constructor() { }

  ngOnInit(): void {
  }

}

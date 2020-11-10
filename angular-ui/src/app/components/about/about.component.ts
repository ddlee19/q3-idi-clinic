import { Component, AfterViewInit } from '@angular/core';
import * as $ from 'jquery';
import * as S from 'semantic-ui-modal'

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements AfterViewInit {

  launchModal() {
    // Sample code from 'https://semantic-ui.com/modules/modal.html#/definition'
  }

  constructor() { }

  ngAfterViewInit(): void {
    this.launchModal()
  }

}

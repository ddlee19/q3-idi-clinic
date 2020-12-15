import { Component } from '@angular/core';

/** The main/parent app component */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  /** The app name. Displayed in the browser tab. */
  title = 'IDI Palm Oil Tracker';

  /** 
   * A boolean indicating whether the brand filter tab is open or closed.
   * Defaults to false.
   */
  showBrands: boolean = false;

  /**
   * A boolean indicating whether the navigation bar is hidden or shown.
   * Defaults to true.
   */
  showNav: boolean = true;

  /**
   * Updates the class variables to hide the navigation bar and open
   * one of the filter panels (e.g., for brands). 
   * 
   * @param value: the name of the filter to open
   */
  openFilter(value: string){
    if(value == 'brands'){
      this.showBrands = true;
      this.showNav = false;
    }
  }

  /**
   * Updates the class variables to hide the currently open filter panel and 
   * show the navigation bar.
   * 
   * @param value: the name of the filter to close
   */
  closeFilter(value: string){
    if(value == 'brands'){
      this.showBrands = false;
      this.showNav = true
    }
  }
}
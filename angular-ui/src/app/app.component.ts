import { Component } from '@angular/core';
declare var $: any 
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'IDI Palm Oil Tracker';
  selectedBrand: number;
  showBrands: boolean = false;
  showNav: boolean = true;

  brandSelected(brandId: number){
    this.selectedBrand = brandId;
  }

  closeBrand(){
    this.selectedBrand = null;
  }

  openFilter(value: string){
    if(value == 'brands'){
      this.showBrands = true;
      this.showNav = false;
    }
  }

  closeFilter(value: string){
    if(value == 'brands'){
      this.showBrands = false;
      this.showNav = true
    }
  }
}
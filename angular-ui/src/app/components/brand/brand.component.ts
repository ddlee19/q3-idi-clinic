import { Component, EventEmitter, Input, OnInit, Output, SimpleChanges } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { DetailedBrand } from '../../interfaces/brands/brand-detailed.interface';


@Component({
  selector: 'app-brand',
  templateUrl: './brand.component.html',
  styleUrls: ['./brand.component.css']
})
export class BrandComponent implements OnInit {

  @Input() selectedBrand: number = null;
  @Output() closeBrandEvent = new EventEmitter();
  brand: DetailedBrand;

  /**
  * Gets a consumer brand from the server by id.
  */
  private async getBrand(brandName: string): Promise<void> {
    if(brandName != null){
      this.brand = await this.apiService.getBrand(brandName);
    }
  }

 /**
 * Emits an event broadcasting that the user has closed the current brand.
 */
 closeBrand(): void {
    this.closeBrandEvent.emit();
  }

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges) {      
    this.getBrand(changes.selectedBrand.currentValue);
  }
}

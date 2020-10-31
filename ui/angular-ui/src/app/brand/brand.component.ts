import { Component, EventEmitter, Input, OnInit, Output, SimpleChanges } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Brand } from '../interfaces/brand.interface';


@Component({
  selector: 'app-brand',
  templateUrl: './brand.component.html',
  styleUrls: ['./brand.component.css']
})
export class BrandComponent implements OnInit {

  @Input() selectedBrand: number = null;
  @Output() closeBrandEvent = new EventEmitter();
  brand: Brand;

  /**
  * Gets a consumer brand from the server by id.
  */
  private async getBrand(brandId: number): Promise<void> {
    if(brandId != null){
      this.brand = await this.apiService.getConsumerBrand(brandId);
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

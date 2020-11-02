import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { BrandFilter } from '../../interfaces/brand-filter.interface';


@Component({
  selector: 'app-brand-filter',
  templateUrl: './brand-filter.component.html',
  styleUrls: ['./brand-filter.component.css']
})
export class BrandFilterComponent implements OnInit {

  filters: BrandFilter[];
  @Input() showBrands: boolean = false;
  @Output() closeFilterEvent = new EventEmitter<string>();
  @Output() brandSelectedEvent = new EventEmitter<number>();

  /**
  * Gets the list of consumer brands from the server.
  */
  private async getBrandFilters(): Promise<void> {
    this.filters = await this.apiService.getBrandFilters();
  }

  /**
  * Emits an event broadcasting that the user has closed the current filter.
  */
  closeFilter(value: string): void {
    this.closeFilterEvent.emit(value);
  }

  /**
  * Emits an event broadcasting that the user has selected a consumer brand.
  */
  openConsumerBrand(brandId: number){
    this.brandSelectedEvent.emit(brandId);
  }

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getBrandFilters();
  }
}

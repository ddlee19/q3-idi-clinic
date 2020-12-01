import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { Brand } from '../../interfaces/brands/brand.interface';


@Component({
  selector: 'app-brand-filter',
  templateUrl: './brand-filter.component.html',
  styleUrls: ['./brand-filter.component.css']
})
export class BrandFilterComponent implements OnInit {

  filters: Brand[];
  @Input() showBrands: boolean = false;
  @Output() closeFilterEvent = new EventEmitter<string>();

  /**
  * Gets the list of consumer brands from the server.
  */
  private async getBrandFilters(): Promise<void> {
    this.filters = await this.apiService.getBrands();
  }

  /**
  * Emits an event broadcasting that the user has closed the current filter.
  */
  closeFilter(value: string): void {
    this.closeFilterEvent.emit(value);
  }

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getBrandFilters();
  }
}

import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { Brand } from '../../interfaces/brands/brand.interface';

/** A component for a brand filter view. */
@Component({
  selector: 'app-brand-filter',
  templateUrl: './brand-filter.component.html',
  styleUrls: ['./brand-filter.component.css']
})
export class BrandFilterComponent implements OnInit {

  /** The list of brands serving as filter options */
  filters: Brand[];

  /** A boolean indicating whether the component should be displayed */
  @Input() showBrands: boolean = false;

  /** Emits the name of a filter when that filter is closed */
  @Output() closeFilterEvent = new EventEmitter<string>();

  /**
  * Retrieves a list of all consumer brands from the API server.
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

  /**
   * The class constructor
   * 
   * @param apiService: An injected instance of the ApiService
   */
  constructor(private apiService: ApiService) {}

   /** 
   * Calls the ApiService to retrieve all brands when Angular begins
   * initializing the component view.
   */
  ngOnInit(): void {
    this.getBrandFilters();
  }
}

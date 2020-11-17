import { AfterViewInit, Component, Input, SimpleChanges } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { MapLayerClient } from './map-layer-client';
import { Mill } from '../../interfaces/mill.interface';
import * as L from 'leaflet';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements AfterViewInit  {
  readonly attribution = 'Tiles &copy; Esri & <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  readonly lightMapUrl = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}';
  readonly labelsUrl = 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}{r}.png';
  readonly darkMapUrl = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png';
  readonly indonesiaLat = -0.7893;
  readonly indonesiaLong = 113.9213;
  readonly initialZoomLevel = 6;
  readonly maxZoom = 20;
 
  @Input() selectedBrand: number;
  private map: L.Map;
  private mapLayerClient: MapLayerClient;
  private millFeatures: Mill[];


  /**
  * Initializes a Leaflet.js map and its layers.
  */
  private async initMap(): Promise<void> {

    // Create light and dark base tile layers
    let lightBaseLayer = L.tileLayer(this.lightMapUrl, { maxZoom: 17, attribution: this.attribution });
    let darkBaseLayer = L.tileLayer(this.darkMapUrl, { attribution: this.attribution });

    // Instantiate map with light base layer
    this.map = L.map("map-id", {
      center: new L.LatLng(this.indonesiaLat, this.indonesiaLong),
      zoom: this.initialZoomLevel,
      layers: [lightBaseLayer]
    });

    // Create mill marker and mill polygon layers
    let millFeatureCollection = await this.apiService.getMills();
    this.millFeatures = millFeatureCollection.features;
    let [allMillsLayer, allMillsRadiiLayer] = this.createMillLayers(this.millFeatures);

    // Instantiate map layer client with default set of layers
    this.mapLayerClient = new MapLayerClient(
      this.map,
      lightBaseLayer,
      darkBaseLayer,
      allMillsLayer,
      allMillsRadiiLayer);
  }

  /**
   * Creates two layers for palm oil mills: (1) a LayerGroup of mill markers
   * and (2) a GeoJSON layer holding the circular areas around each mill.
   * 
   * @param millFeatures: a list of mill features 
   */
  private createMillLayers(millFeatures: Mill[]): [L.LayerGroup, L.GeoJSON] {
    let markers = [];
    let radiiLayer = L.geoJSON(null, { style: this.getMillStyleObject });

    millFeatures.forEach(m => {
      let mill = m.properties;
      let marker = L.marker(
          [mill.latitude, mill.longitude], 
          {icon: this.styleMillMarker(m)}
        )
        .bindPopup(`
          <div>
            <h4>
              ${mill.mill_name}<br/>
              <span style="color:grey;">
                ${mill.sub_state.toUpperCase()}, ${mill.state.toUpperCase()}
              </span><br/>
              Past Risk Score: ${mill.risk_score_past}<br/>
              Current Risk Score: ${mill.risk_score_current}<br/>
              Future Risk Score: ${mill.risk_score_future}
            </h4>
          <div>
        `);

        markers.push(marker);
        radiiLayer.addData(<any>m);
      });

      return [L.layerGroup(markers), radiiLayer];
  }


  /**
  * Returns a style object for a mill based on its future risk score.
  */
  private getMillStyleObject(millFeature: any): object{
    let score = millFeature.properties.risk_score_current;

    if (score == 1) {
      return {color: "#ffc743", fillColor:"#ffc743", opacity: 0.1};
    }
    else if (score == 2){
      return {color: "#fb7337", fillColor:"#fb7337", opacity: 0.1};
    }
    else if (score == 3){
      return {color: "#f60b28", fillColor:"#f60b28", opacity: 0.1};
    }
    else if (score == 4){
      return {color: "#95081b", fillColor:"#95081b", opacity: 0.1};
    }
    else {
      return {color: "#620000", fillColor:"#620000", opacity: 0.1};
    }
  }

  /**
  * Builds a custom HTML/CSS-only icon for a mill marker.
  */
  private styleMillMarker(millFeature: Mill): L.DivIcon{
    let style = this.getMillStyleObject(millFeature);

    let markerHtmlStyles = `
      background-color: ${style["fillColor"]};
      width: 2rem;
      height: 2rem;
      display: block;
      left: -1.5rem;
      top: -1.5rem;
      position: relative;
      border-radius: 3rem 3rem 0;
      transform: rotate(45deg);
      box-shadow: inset 11px 5px 13px 0px rgba(0,0,0,0.48)`

    return new L.DivIcon({
      className: "my-custom-pin",
      iconAnchor: [0, 0],
      popupAnchor: [0, -36],
      html: `<span style="${markerHtmlStyles}" />`
    })
  }

  /**
  * Filters mill markers displayed on the map by brand.
  */
  private filterMills(brandId: number): void{

    // If user clears brand selection, reset to default view showing all mills
    if (brandId == null){
      this.mapLayerClient?.resetMillsLayers();
      return;
    }

    // Otherwise, filter by brand
    let filteredMillFeatures = this.millFeatures.filter(mill => {
      let brand_ids = mill.properties.brand_ids;
      if (brand_ids !== null && brand_ids.includes(brandId)){
        return mill;
      }
    });

    // Create new filtered layers
    let filteredLayers = this.createMillLayers(filteredMillFeatures);
    let filteredMillsLayer = filteredLayers[0];
    let filteredMillsRadiiLayer = filteredLayers[1];

    // Replace any existing mill layers with filtered layers
    this.mapLayerClient.filterMillsLayers(filteredMillsLayer, 
                                          filteredMillsRadiiLayer);
  }

  /**
   * The class constructor
   * @param apiService An injected instance of the ApiService
   */
  constructor(private apiService: ApiService) {}

  /** Initializes Leaflet map with layers after DOM loads */ 
  ngAfterViewInit(): void {
    this.initMap();
  }

  /**
   * Tracks class property changes in order to perform updates
   * @param changes 
   */
  ngOnChanges(changes: SimpleChanges) {
    if(this.map !== null && this.mapLayerClient !== null){
      this.filterMills(changes.selectedBrand.currentValue);
    }
  }
}

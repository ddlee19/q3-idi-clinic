import * as L from 'leaflet';

/**
 * Manages the removal and addition of layers to a Leaflet map instance.
 */
export class MapLayerClient {

    map: L.Map;
    light_base_layer: L.TileLayer;
    dark_base_layer: L.TileLayer;
    all_mills_layer: L.LayerGroup;
    all_mills_radii_layer: L.GeoJSON;
    filtered_mills_layer: L.LayerGroup;
    filtered_mills_radii_layer: L.LayerGroup;

    constructor(
        map: L.Map,
        light_base_layer: L.TileLayer,
        dark_base_layer: L.TileLayer,
        all_mills_layer: L.LayerGroup,
        all_mills_radii_layer: L.GeoJSON)
    {
        this.map = map;
        this.all_mills_layer = all_mills_layer;
        this.all_mills_radii_layer = all_mills_radii_layer;
        this.light_base_layer = light_base_layer;
        this.dark_base_layer = dark_base_layer;
        this.initializeOverlayLayers();
    }

    private initializeOverlayLayers(){
        this.map.addLayer(this.all_mills_radii_layer);
        this.map.addLayer(this.all_mills_layer);
    }

    private removeLayerIfActive(layer: L.Layer){
        if(layer !== null && this.map.hasLayer(layer)){
            this.map.removeLayer(layer);
        }
    }

    private clearMillsLayers(){
        this.removeLayerIfActive(this.all_mills_layer);
        this.removeLayerIfActive(this.all_mills_radii_layer);
        this.removeLayerIfActive(this.filtered_mills_layer);
        this.removeLayerIfActive(this.filtered_mills_radii_layer);
    }

    resetMillsLayers(){
        this.clearMillsLayers();
        this.map.addLayer(this.all_mills_radii_layer);
        this.map.addLayer(this.all_mills_layer);
    }

    filterMillsLayers(
        filtered_mills_layer: L.LayerGroup,
        filtered_mills_radii_layer: L.LayerGroup)
    {
        this.clearMillsLayers();

        this.filtered_mills_radii_layer = filtered_mills_radii_layer;
        this.map.addLayer(this.filtered_mills_radii_layer);

        this.filtered_mills_layer = filtered_mills_layer;
        this.map.addLayer(this.filtered_mills_layer);
    }
}


import * as L from 'leaflet';

/**
 * Manages the removal and addition of layers to a Leaflet map instance.
 */
export class MapLayerClient {

    map: L.Map;
    baseLayer: L.TileLayer;
    allMillsLayer: L.LayerGroup;
    allMillsBoundariesLayer: L.GeoJSON;
    filteredMillsLayer: L.LayerGroup;
    filteredMillsBoundariesLayer: L.LayerGroup;

    constructor(
        map: L.Map,
        baseLayer: L.TileLayer,
        allMillsLayer: L.LayerGroup,
        allMillsBoundariesLayer: L.GeoJSON)
    {
        this.map = map;
        this.baseLayer = baseLayer;
        this.allMillsLayer = allMillsLayer;
        this.allMillsBoundariesLayer = allMillsBoundariesLayer;
        this.initializeOverlayLayers();
    }

    private initializeOverlayLayers(){
        this.map.addLayer(this.allMillsBoundariesLayer);
        this.map.addLayer(this.allMillsLayer);
    }

    private removeLayerIfActive(layer: L.Layer){
        if(layer !== null && this.map.hasLayer(layer)){
            this.map.removeLayer(layer);
        }
    }

    private clearMillsLayers(){
        this.removeLayerIfActive(this.allMillsLayer);
        this.removeLayerIfActive(this.allMillsBoundariesLayer);
        this.removeLayerIfActive(this.filteredMillsLayer);
        this.removeLayerIfActive(this.filteredMillsBoundariesLayer);
    }

    resetMillsLayers(){
        this.clearMillsLayers();
        this.map.addLayer(this.allMillsBoundariesLayer);
        this.map.addLayer(this.allMillsLayer);
    }

    filterMillsLayers(
        filteredMillsLayer: L.LayerGroup,
        filteredMillsBoundariesLayer: L.LayerGroup)
    {
        this.clearMillsLayers();

        this.filteredMillsBoundariesLayer = filteredMillsBoundariesLayer;
        this.map.addLayer(this.filteredMillsBoundariesLayer);

        this.filteredMillsLayer = filteredMillsLayer;
        this.map.addLayer(this.filteredMillsLayer);
    }
}


import * as L from 'leaflet';

/**
 * Manages the removal and addition of layers to a Leaflet map instance.
 * Note: Mill markers and their boundaries exist in separate map layers
 * because they are two different Leaflet layer types (i.e., a LayerGroup
 * and a GeoJSON layer, respectively).
 */
export class MapLayerClient {

    map: L.Map;
    baseLayer: L.TileLayer;
    allMillsLayer: L.LayerGroup;
    allMillsBoundariesLayer: L.GeoJSON;
    filteredMillsLayer: L.LayerGroup;
    filteredMillsBoundariesLayer: L.LayerGroup;

    /**
     * The class constructor.
     * 
     * @param map: A reference to the Leaflet map instance
     * @param baseLayer: The base tile layer (satellite imagery)
     * @param allMillsLayer: The layer containing all mill markers
     * @param allMillsBoundariesLayer: The layer containing all mill boundaries
     */
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

    /** 
     * Initializes two layers, the "allMillsLayer" and the
     * "allMillsBoundariesLayer,"" on the Leaflet map instance.
     */
    private initializeOverlayLayers(){
        this.map.addLayer(this.allMillsBoundariesLayer);
        this.map.addLayer(this.allMillsLayer);
    }

    /**
     * Removes the given layer from the map if it is currently there.
     * 
     * @param layer: A Leaflet map layer
     */
    private removeLayerIfActive(layer: L.Layer){
        if(layer !== null && this.map.hasLayer(layer)){
            this.map.removeLayer(layer);
        }
    }

    /** Removes all layers from the map except the base tile layer. */
    private clearMillsLayers(){
        this.removeLayerIfActive(this.allMillsBoundariesLayer);
        this.removeLayerIfActive(this.allMillsBoundariesLayer);
        this.removeLayerIfActive(this.filteredMillsLayer);
        this.removeLayerIfActive(this.filteredMillsBoundariesLayer);
    }

    /** 
     * Removes the layers of filtered mills and filtered mill boundaries
     * and then adds the "allMillsBoundariesLayer" and "allMillsBoundariesLayer"
     * back in sequence--essentially resetting the view.
     */
    resetMillsLayers(){
        this.clearMillsLayers();
        this.map.addLayer(this.allMillsBoundariesLayer);
        this.map.addLayer(this.allMillsLayer);
    }

    /**
     * Updates the map to show a filtered mills layer and its corresponding 
     * filtered mill boundaries layer.
     * 
     * @param filteredMillsLayer: The layer of filtered mills to add to the map
     * @param filteredMillsBoundariesLayer: The layer of filtered mill boundaries
     *                                      to add to the map
     */
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


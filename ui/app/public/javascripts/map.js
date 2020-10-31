const LIGHT_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png';
const DARK_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png';
const INDONESIA_COORDS = [-0.7893, 113.9213];
const INITIAL_ZOOM_LEVEL = 6;
const MAX_ZOOM = 20;
const ATTRIBUTION = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

// Create light and dark base tile layers
let lightMap = L.tileLayer(LIGHT_MAP_URL, {attribution: ATTRIBUTION});
let darkMap = L.tileLayer(DARK_MAP_URL, {attribution: ATTRIBUTION});

// Instantiate map
let webmap = L.map("map-id", {
	center: INDONESIA_COORDS,
	zoom: INITIAL_ZOOM_LEVEL,
	layers: [lightMap]
});

// Retrieve GEE tiles
let tileUrlJSON = JSON.parse(document.getElementById("map-script-id").getAttribute("data-tile-urls"));

// Add treecover 2000 layer
treecover2000Url = tileUrlJSON["treecover2000"];
treecover2000Layer = L.tileLayer(treecover2000Url, { attribution: ATTRIBUTION});
treecover2000Layer.addTo(webmap);

// Add treecover loss layers
let treeLossMaps = []
Object.keys(tileUrlJSON).forEach(layerName => {
	if(layerName != "treecover2000"){
		tileUrl = tileUrlJSON[layerName];
		treeLossLayer = L.tileLayer(tileUrl, { attribution: ATTRIBUTION});
		//treeLossLayer.addTo(webmap);
		treeLossMaps.push(treeLossLayer);
	}
})

// Group tree loss layers
treelossGroup = L.layerGroup(treeLossMaps)
treelossGroup.addTo(webmap)

// Set up layer control
let baseMaps = {"Light": lightMap, "Dark": darkMap};
let overlayMaps = {
	"Treecover 2000": treecover2000Layer, 
	"Treecover Loss" : treelossGroup
};
//L.control.layers(baseMaps, overlayMaps).addTo(webmap);

// bind events to buttons
$("input[name='treecover2000']")
	.on('click', function() {
		if(webmap.hasLayer(treecover2000Layer)) {
			$(this).removeClass('checked');
			webmap.removeLayer(treecover2000Layer);
		} else {
			webmap.addLayer(treecover2000Layer);        
			$(this).addClass('checked');
		}
	}
);

// bind events to buttons
webmap.eachLayer(function(layer) { console.log(layer)})
$("input[name='treecoverloss']")
	.on('click', function() {
		if(webmap.hasLayer(treelossGroup)) {
			$(this).removeClass('checked');
			webmap.removeLayer(treelossGroup);
		} else {
			webmap.addLayer(treelossGroup);        
			$(this).addClass('checked');
		}
	}
);

// Add markers
let millsDictJSON = JSON.parse(document.getElementById("map-script-id").getAttribute("data-mills-dict-str"));
let markers = [];
Object.keys(millsDictJSON).forEach(key => {
	let mill = millsDictJSON[key];
	let marker = L.marker([mill["latitude"], mill["longitude"]])
		.bindPopup(`
			<div>
				<h3>
					${mill["mill_name"]}<br/>
					<span style="color:grey;">
						${mill["sub_state"].toUpperCase()}, ${mill["state"].toUpperCase()}
					</span>
				</h3>
			<div>
		`);
	markers.push(marker);
});

// Create map layers
let markerLayer = L.layerGroup(markers);
markerLayer.addTo(webmap)

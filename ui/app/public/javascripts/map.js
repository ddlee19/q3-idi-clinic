const LIGHT_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png';
const DARK_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png';
const INDONESIA_COORDS = [-0.7893, 113.9213];
const INITIAL_ZOOM_LEVEL = 6;
const MAX_ZOOM = 20;

// Instantiate map
let webmap = L.map("map-id").setView(INDONESIA_COORDS, INITIAL_ZOOM_LEVEL);
L.tileLayer(LIGHT_MAP_URL, { maxZoom: MAX_ZOOM }).addTo(webmap);

// Add markers
let millsDictJSON = JSON.parse(document.getElementById("map-script-id").getAttribute("data-mills-dict-str"));
let markers = [];
Object.keys(millsDictJSON).forEach(key => {
	let mill = millsDictJSON[key];
	let marker = L.marker([mill["latitude"], mill["longitude"]])
		.addTo(webmap)
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
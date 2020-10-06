const INDONESIA_COORDS = [-0.7893, 113.9213];
const INITIAL_ZOOM_LEVEL = 6;
const LIGHT_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png';
const DARK_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png';

// Instantiate map
let webmap = L.map("map-id").setView(INDONESIA_COORDS, INITIAL_ZOOM_LEVEL);
L.tileLayer(LIGHT_MAP_URL, { maxZoom: 20 }).addTo(webmap);

// Add markers
let millsDictJSON = JSON.parse(document.getElementById("mills-dict").value);
let markers = [];
Object.keys(millsDictJSON).forEach(key => {
	let mill = millsDictJSON[key];
	console.log(mill)
	let latitude = mill["properties"]["latitude"];
	let longitude = mill["properties"]["longitude"];
	let marker = L.marker([latitude, longitude]).addTo(webmap);
	markers += marker;
});

let markerLayer = L.layerGroup(markers);
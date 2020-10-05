const INDONESIA_COORDS = [-0.7893, 113.9213];
const INITIAL_ZOOM_LEVEL = 6;
const LIGHT_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png';
const DARK_MAP_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png';

var webmap = L.map('mapid').setView(INDONESIA_COORDS, INITIAL_ZOOM_LEVEL);

L.tileLayer(DARK_MAP_URL, {
	maxZoom: 20,
	attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
}).addTo(webmap);
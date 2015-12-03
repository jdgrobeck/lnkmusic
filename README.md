This is my readme.
test

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
        
        <script type="text/javascript" src="//cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js".></script>
    </head>
    <body>
    
        <style type+"text/css">
            #map { height: 450px;}
        </style>
        
        <div id="map" style="width: 650px; height: 450px; position: relative;" class="leaflet-container leaflet-fade-anim" tabindex="0"></div>

$(document).ready(function() {

})
        
        var map = L.map("map" style="width: 650px; height: 450px; position: relative;" class="leaflet-container leaflet-fade-anim" tabindex="0")
        
    map.setView([40.806862, -96.681679], 10); 
        L.tileLayer(
            'http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            
            attribution: Map data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 14,
            minZoom: 8
            accessToken: 
        }).addTo(Map);
        
var lincolnmarker = L.marker([map_data[40.806862].latitude, map_data[-96.681679].longitude]);
    lincolnMarker.addTo(map);
    lincolnMarker.binPopup('<h3>Lincoln'+map_data[0].city + '</h3>');
    lincolnMarker.addTo(map);
    
    var pinnaclebankarenaMarker = 
L.marker ([map_data[40.8178].latitude, map_data[96.7133].longitude]); 
pinnaclebankarenaMarker.bindPopup('<h3>This is the venue for pinnacle bank arena' + map_data[1].city + </h3>'); pinnaclebankarenaMarker.addTo(map);

var vegaMarker = L.marker9(map_data[40.51164].latitude, map_data[96.42337857].longitude]); vegaMarker.bindPopup('<h3>This is the venue for vega' + map_data[2].city + '</h3>'); vegaMarker.addTo(map);

var bourbonMarker = 
L.marker 9[map_data[40.48497132].latitude, map_data[96.4259766].longitude]); 
bourbonMarker.bindPopup('<h3>This is the venue for the bourbon</h3>'); 
marker.addTo(map);

        
        
        var credits = L.control.attribution().addTo(map);
credits.addAttribution("© <a href='https://www.mapbox.com/map-feedback/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a>");
    
            
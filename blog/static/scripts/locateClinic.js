var map;
var service;
var infowindow;
var pos;
var request;
var place;
var Circle;


function initMap(){
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
          lat: -34.397,
          lng: 150.644
        },
        zoom: 15
});
infoWindow = new google.maps.InfoWindow;

getLocation();


function getLocation(){
      // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      console.log("getLocation:" + pos.lat + "," + pos.lng);
      var marker = new google.maps.Marker({
        position: pos,
        map: map,
        icon: "http://maps.google.com/mapfiles/ms/micons/blue.png"
      });

      infoWindow.setPosition(pos);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(pos);
      getNearByPlaces(pos);
    }, function() {
      console.log("calling handleLocationError(true)");
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    console.log("calling handleLocationError(false)")
    handleLocationError(false, infoWindow, map.getCenter());
  }
  infowindow = new google.maps.InfoWindow();
}


}
function getNearByPlaces(pos){
    console.log("getNearByPlaces:" + pos.lat + "," + pos.lng);
  request = {   
       // location should be cetnered based on user's location.
    location: pos,
     // enter radius which is in meters
    radius: '1000',
     // determines the place we are searching for 
    query: ['hospital','clinic']
    };

    // create a service using the Places API
    service = new google.maps.places.PlacesService(map);
     // searches for the request and callback that ensures location was located accurately
    // service.textSearch(request, callback);
    service.textSearch(request, callback );}

function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
      console.log("callback received " + results.length + " results");
      var bounds = new google.maps.LatLngBounds();
      for (var i = 0; i < results.length; i++) {
        console.log(JSON.stringify(results[i]));
        place = results[i];
        
        var mark = createMarker(results[i]);
        bounds.extend(mark.getPosition());
      }
      map.fitBounds(bounds);
    } else console.log("callback.status=" + status);
  }

  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
      'Error: The Geolocation service failed.' :
      'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
  }

  
  function createMarker(place) {
    var marker = new google.maps.Marker({
     
      map: map,
      position: place.geometry.location,
      fields: ['name', 'formatted_address'],
      animation: google.maps.Animation.DROP,
      // icon: "http://maps.google.com/mapfiles/ms/micons/red.png"
    });
  
    // google.maps.event.addListener(marker, 'click', function() {
    //   infowindow.setContent(place.name);
    //   infowindow.open(map, this);
    // });

    google.maps.event.addListener(marker, 'click', function() {
            
      infowindow.setContent('<div><strong>' + place.name +'<br>' + place.formatted_address  + '</strong><br>' + '</div>');
      infowindow.open(map, this);
  });
    return marker;
  }
/*
if (window.navigator) {
    window.navigator.geolocation.getCurrentPosition(successcallback, failurecallback);
}
else{
    alert("unsuccess...");
}
const successcallback = (position) => {
    alert("success....");
    console.log(position);
    const { latitude, longitude } = position.coords;
    console.log("longitude");
    console.log(longitude);
    
}

function clicked(){
    alert("running....");
    document.getElementById("coor1").innerHTML = longitude;
    document.getElementById("coor2").innerHTML = latitude;
    document.getElementById("pos").innerHTML = position;
    document.getElementById("update").innerHTML = "1";
}
*/
const options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };
  
  function success(pos) {
    const crd = pos.coords;
  
    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
    alert(crd.longitude)
    document.getElementById("coor1").innerHTML = crd.latitude;
    document.getElementById("coor2").innerHTML = crd.longitude;

  }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }
  
  navigator.geolocation.getCurrentPosition(success, error, options);
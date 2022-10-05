
if (window.navigator) {
    window.navigator.geolocation.getCurrentPosition(successcallback, failurecallback);
}
const successcallback = (position) => {
    console.log(position);
    const { latitude, longitude } = position.coords;
    document.getElementById("coor").innerHTML = longitude, latitude;
}
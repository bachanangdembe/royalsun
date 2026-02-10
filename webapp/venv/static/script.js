document.getElementById("getLocation").addEventListener("change", function () {
  if (this.checked) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          document.getElementById("lat").value = pos.coords.latitude;
          document.getElementById("lng").value = pos.coords.longitude;
        },
        (err) => {
          alert("Location access denied or not available");
          console.log(err);
        },
        { enableHighAccuracy: true, timeout: 10000 }
      );
    } else {
      alert("Geolocation not supported by browser");
    }
  }
});

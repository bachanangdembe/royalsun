const cb = document.getElementById("getLocation");
cb?.addEventListener("change", function () {
  if (!this.checked) return;
  if (!navigator.geolocation) return alert("Geolocation not supported");
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      lat.value = pos.coords.latitude.toFixed(6);
      lng.value = pos.coords.longitude.toFixed(6);
    },
    () => alert("Location permission denied"),
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
  );
});

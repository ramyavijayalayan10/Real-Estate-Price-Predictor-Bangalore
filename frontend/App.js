function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_house_price";// Use this if you're NOT using nginx
  // var url = "/api/predict_home_price"; // Uncomment if using nginx

  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>₹ " + data.estimated_price.toString() + " Lakh</h2>";
    console.log(status);
  });
}

function onClickedResetForm() {
  document.getElementById("uiSqft").value = "";

  var bhkRadios = document.getElementsByName("uiBHK");
  for (var i = 0; i < bhkRadios.length; i++) bhkRadios[i].checked = false;

  var bathRadios = document.getElementsByName("uiBathrooms");
  for (var i = 0; i < bathRadios.length; i++) bathRadios[i].checked = false;

  document.getElementById("uiLocations").selectedIndex = 0;
  document.getElementById("uiEstimatedPrice").innerHTML = "";

  console.log("Form has been reset.");
}

function onPageLoad() {
  console.log("document loaded");

  // ⬇️ Reset form on page load
  document.getElementById("uiSqft").value = "";
  document.getElementsByName("uiBHK").forEach(r => r.checked = false);
  document.getElementsByName("uiBathrooms").forEach(r => r.checked = false);
  document.getElementById("uiLocations").selectedIndex = 0;
  document.getElementById("uiEstimatedPrice").innerHTML = "";
  var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you're NOT using nginx
  // var url = "/api/get_location_names"; // Uncomment if using nginx

  $.get(url, function(data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      if (!uiLocations) {
        console.error("Dropdown element with id='uiLocations' not found");
      }
      $('#uiLocations').empty();
      $('#uiLocations').append(new Option("Choose a Location", "", false, false)); // Placeholder
      locations.forEach(function(location) {
        $('#uiLocations').append(new Option(location));
      });
    }
  });
}

window.onload = onPageLoad;


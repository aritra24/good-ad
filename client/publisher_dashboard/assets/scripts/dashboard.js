window.onload = function () {
  var adServed = document.querySelector("#ad-served");
  var adClicks = document.querySelector("#ad-clicks");
  var adActions = document.querySelector("#ad-actions");
  var adConversion = document.querySelector("#ad-conversions");
  var publisherId = 2;
  var url = `http://localhost:5000/getPublisherProfile?publisherId=${publisherId}`;
  fetch(url, {
    headers: {
      "Content-type": "application/json",
    },
    mode: "cors",
    method: "GET",
  })
    .then((res) => res.json())
    .then((res) => {
      adServed.innerHTML = res.ads;
      adClicks.innerHTML = res.click_throughs;
      adActions.innerHTML = res.actions;
      adConversion.innerHTML = "$" + res.total_due;
    });
};

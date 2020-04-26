window.onload = function () {
  var urlParams = new URLSearchParams(window.location.search);
  // var ngoid = urlParams.get("ngoid");
  // var publisherid = urlParams.get("publisherid");
  var ngoid = 1;
  var publisherid = 2;
  var url = `http://localhost:5000/getNgoDetails?ngoId=${ngoid}&publisherId=${publisherid}`;
  fetch(url, {})
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
    });

  var donateBtn = document.querySelector("#donate-btn");
  donateBtn.addEventListener("click", (e) => {
    e.preventDefault();
    var url = `http://localhost:5000/recordPayment`;
    var body = {
      ngoId: ngoid,
      publisherId: publisherid,
    };
    var fields = $("form").serializeArray();
    for (var i = 0; i < fields.length; i++) {
      body[fields[i]["name"]] = fields[i]["value"];
    }

    fetch(url, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    }).then(() => {
      this.alert(
        "Thank you for donating to GiveHope! This form will redirect to the payment gateway"
      );
    });
  });
};

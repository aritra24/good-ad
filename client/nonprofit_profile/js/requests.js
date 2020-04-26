window.onload = function () {
  var urlParams = new URLSearchParams(window.location.search);
  var ngoid = urlParams.get("ngoid");
  var publisherid = urlParams.get("publisherid");

  function getAttrs(DOMelement) {
    var obj = {};
    $.each(DOMelement.attributes, function () {
      if (this.specified) {
        obj[this.name] = this.value;
      }
    });
    return obj;
  }

  var url = `http://localhost:3000/getNgoDetails?ngoid=${ngoid}&publisherid=${publisherid}`;
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
      ngoid: ngoid,
      pubisherid: publisherid,
    };
    var fields = $("form").serializeArray();
    for (var i = 0; i < fields.length; i++) {
      body[fields[i]["name"]] = fields[i]["value"];
    }

    fetch("http://localhost:5000/recordPayment", {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
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

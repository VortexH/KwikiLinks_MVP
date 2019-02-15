/* TODO: add event listeners for on click and close */

//grabbing the text inputs
let firstw = document.getElementById('firstw');
let lastw = document.getElementById('lastw');

//grabbing the button
let sendMessageButton = document.getElementById('sendMessageButton');

sendMessageButton.onclick = function (el) {
  console.log(el);
  console.log(firstw.value);
  console.log(lastw.value);

  let data = {
    firstw: firstw.value,
    lastw: lastw.value
  }

  fetch("/kwiklinks", {
    method: "POST",
    headers: new Headers({ 'content-type': 'application/json' }),
    body: JSON.stringify(data)
  }).then(function (response) {
    // catch return from server promise, pullout json
    return response.json();
  }).then(function (myJson) {
    // append results to ul so that we know servers do things
    console.log(JSON.stringify(myJson));
    let resList = document.getElementById('results-ul');
    //foreach does a loop through the response json from the server, appending each to the ul
    Object.keys(myJson).forEach(function (item, key) {
      console.log(key);
      console.log(item);
      console.log(myJson[item]);
      let li = document.createElement("li");
      li.appendChild(document.createTextNode(item + ": " + myJson[item]));
      resList.appendChild(li);
    });
  });
};

// Email Subscription
let email = document.getElementById('inputEmail');
let subscribeButton = document.getElementById('subscribeButton');

subscribeButton.onclick = function (el) {
  console.log(el);
  console.log(email.value);

  let data = {
    email: email.value
  }

  fetch("/emailsubscribe", {
    method: "POST",
    headers: new Headers({ 'content-type': 'application/json' }),
    body: JSON.stringify(data)
  }).then(function (response) {
    // catch return from server promise, pullout json
    return response.json();
  });
};

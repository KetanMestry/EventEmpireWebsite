

// function changeCharacterAnim() {
//   document.getElementById('homeCharacter').src = "{% static 'images/searchingSanta.png' %}";
//   // console.log("changed");
// }

let selectedVal = 0;

function changeHomeCharacter(value) {

  let santa = "static/images/ani1.png";
  let partyGuy = "static/images/partyChar.png";


  value == 1 ? document.getElementById('homeCharacter').setAttribute("src", santa) : document.getElementById('homeCharacter').setAttribute("src", partyGuy);


    // selectedVal = value;
}


function changePartyListCharacter(value) {
  let santa = "static/images/ani2.png";
  let partyGuy = "static/images/partyCharWithBear.png";

  value == 1 ? document.getElementById('partyListCharacter').setAttribute("src", santa) : document.getElementById('partyListCharacter').setAttribute("src", partyGuy);

  selectedVal = value;
}


// selectedVal == 1 ? document.getElementById('partyListCharacter').src = "static/images/ani2.png" : document.getElementById('partyListCharacter').src = "{% static 'images/partyCharWithBear.png' %}";



// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune').then(res => res.json()).then(data =>  data.data[0].latitude);

// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune');

// console.log(dataObj.data)
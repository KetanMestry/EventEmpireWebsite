

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
  let santa = "/static/images/ani2.png";
  let partyGuy = "/static/images/partyCharWithBear.png";

  value == 1 ? document.getElementById('partyListCharacter').setAttribute("src", santa) : document.getElementById('partyListCharacter').setAttribute("src", partyGuy);

  selectedVal = value;
}


// selectedVal == 1 ? document.getElementById('partyListCharacter').src = "static/images/ani2.png" : document.getElementById('partyListCharacter').src = "{% static 'images/partyCharWithBear.png' %}";



// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune').then(res => res.json()).then(data =>  data.data[0].latitude);

// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune');

// console.log(dataObj.data)




// Get parties data
function searchParties(){
  let elem = document.getElementById("partyTypeSelector");
  let elemTwo = document.getElementById("selectedCity");
  let partyStartDate;
  if(elem.value == 1){
    partyStartDate = "2022-12-24";
  }else{
    partyStartDate = "2022-12-24";
  }

  let city = elemTwo.innerHTML;
  
}

function ChangeState(){
  let btn = document.getElementById("stateButton").click();
}



function cardClicked(){
  elem =  document.getElementById("cardButton")
  console.log(elem)
}




function changeAmount(){
  let elem = document.getElementById('amountID');
  let elemMem = document.getElementById('inputMembers');

  let amount = elem.innerHTML;
  let members = elemMem.innerHTML;

  let totalAmount = amount * members;

  elem.innerText = totalAmount;

  console.log(totalAmount)
}


// Chatbot
function showhideimg() {
  var img = document.getElementById("chatbotimg");
  var chatwindow = document.getElementById("chatwindow");
  var closeimg = document.getElementById("closeimg");
  if (img.style.display === "none") {
      img.style.display = "block";
      chatwindow.style.display = "none";
      closeimg.style.display = "none"
  }
  else {
      img.style.display = "none";
      chatwindow.style.display = "block";
      closeimg.style.display = "block";
  }
}

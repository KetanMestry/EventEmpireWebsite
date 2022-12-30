

// function changeCharacterAnim() {
//   document.getElementById('homeCharacter').src = "{% static 'images/searchingSanta.png' %}";
//   // console.log("changed");
// }


function changeHomeCharacter(value) {

  let santa = "static/images/ani1.png";
  let partyGuy = "static/images/partyChar.png";


  value == 1 ? document.getElementById('homeCharacter').setAttribute("src", santa) : document.getElementById('homeCharacter').setAttribute("src", partyGuy);

  
}


function changePartyListCharacter(value) {
  let santa = "/static/images/ani2.png";
  let partyGuy = "/static/images/partyCharWithBear.png";

  value == 1 ? document.getElementById('partyListCharacter').setAttribute("src", santa) : document.getElementById('partyListCharacter').setAttribute("src", partyGuy);
  let btnOne = document.getElementById("xMasBtn");
  let btnTwo = document.getElementById("newYearBtn");
  if(value == 1){
      if(!btnOne.classList.contains("btn-dark"))
      {
         btnOne.classList.add("btn-dark");
         btnTwo.classList.remove("btn-dark")
         btnOne.classList.remove("btn-outline-dark")
      }else{
        btnOne.classList.add("btn-outline-dark");
        btnTwo.classList.remove("btn-outline-dark");
        btnOne.classList.remove("btn-dark");
      }
  }else{
    if(!btnTwo.classList.contains("btn-dark"))
    {
       btnTwo.classList.add("btn-dark");
       btnOne.classList.remove("btn-dark");
       btnTwo.classList.remove("btn-outline-dark")
    }else{
      btnTwo.classList.add("btn-outline-dark");
      btnOne.classList.remove("btn-outline-dark");
      btnTwo.classList.remove("btn-dark")
    }
  }
 
}


function selectedParty(value){

  let btnOne = document.getElementById("xMasBtn");
  let btnTwo = document.getElementById("newYearBtn");
  if(value == "1"){
    btnOne.classList.add("btn-dark");
    btnTwo.classList.add("btn-outline-dark")
   
  }else{
    btnTwo.classList.add("btn-dark");
    btnOne.classList.add("btn-outline-dark")
  }
}





// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune').then(res => res.json()).then(data =>  data.data[0].latitude);

// let dataObj =  fetch('http://api.positionstack.com/v1/forward?access_key=62f71233d2704bcee650df75457205b4&query=Cafe CO2, Pune');

// console.log(dataObj.data)







function cardClicked() {
  elem = document.getElementById("cardButton")
  console.log(elem)
}




function changeAmount() {
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

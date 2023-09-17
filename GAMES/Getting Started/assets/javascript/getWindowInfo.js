/* Function to get and display information about the whole window 
    and also to display the play area and the image with it. */

function displayGameInfo() {
  /* Get and display information about the whole window */

  document.getElementById("height").innerHTML = window.innerHeight;
  document.getElementById("width").innerHTML = window.innerWidth;

  /* Get and display information about the Play Area */
  let areaHeight = document.getElementById("playArea").offsetHeight;
  let areaWidth = document.getElementById("playArea").offsetWidth;
  document.getElementById("areaHeight").innerHTML = areaHeight + "px";
  document.getElementById("areaWidth").innerHTML = areaWidth + "px";

  let areaXPos = document.getElementById("playArea").offsetTop;
  let areaYPos = document.getElementById("playArea").offsetLeft;
  document.getElementById("areaXPos").innerHTML = areaXPos + "px";
  document.getElementById("areaYPos").innerHTML = areaYPos + "px";

  /* Get and display information about the IMG object */
  let boyHeight = document.getElementById("boyWalkingRight").offsetHeight;
  let boyWidth = document.getElementById("boyWalkingRight").offsetWidth;
  document.getElementById("boyHeight").innerHTML = boyHeight + "px";
  document.getElementById("boyWidth").innerHTML = boyWidth + "px";

  let boyXPos = document.getElementById("boyWalkingRight").offsetTop;
  let boyYPos = document.getElementById("boyWalkingRight").offsetLeft;
  document.getElementById("xPos").innerHTML = boyXPos + "px";
  document.getElementById("yPos").innerHTML = boyYPos + "px";
}

displayGameInfo();

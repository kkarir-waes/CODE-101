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

function setLeft(id, x) {
  document.getElementById(id).style.left = x + "px";
}
function setTop(id, y) {
  document.getElementById(id).style.top = y + "px";
}

function startUp() {
  moveObject();
  gameTimer = window.setInterval(displayTime, 1000);
}

function displayTime() {
  gameTime++;
  document.getElementById("time_tb").innerText = "Time " + gameTime;
}

function moveObject() {
  let w = window.outerWidth;
  let h = window.outerHeight;
  atomX = randomNumber(2, 16);

  atomY = randomNumber(2, 16);

  setLeft("atom", 20 * atomX);
  setTop("atom", 20 * atomY);
}

function handleKeys(e) {
  if (e.keyCode == 37) {
    ufoX--;
  }
  if (e.keyCode == 39) {
    ufoX++;
  }
  if (e.keyCode == 38) {
    ufoY--;
  }
  if (e.keyCode == 40) {
    ufoY++;
  }

  setLeft("ufo", 20 * ufoX);
  setTop("ufo", 20 * ufoY);
}

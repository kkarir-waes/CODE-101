/* key handler for arrow keys and space-bar */

/* define globl variables */
var keyPressed = "";
var xPos = 0,
  yPos = 0;

var minXPos = 0;
var minYPos = 0;

var maxXPos = 100;
var maxYPos = 100;

/* set the horizontal position of the character */
function setLeft(id, x) {
  document.getElementById(id).style.left = x + "px";
}

/* set the vertical position of the character */
function setTop(id, y) {
  document.getElementById(id).style.top = y + "px";
}

/* Process arrow keys pressed */
function handleArrowKeys(e) {
  /* event Listener for keydown returns 'e' which has a keycode attached.
     using that keycode, it's possible to know which key was pressed.
     Here we are interested only in arrow keys.             */

  switch (e.keyCode) {
    case 32 /* space bar */:
      keyPressed = "space";
      break;

    case 37 /* left arrow */:
      keyPressed = "left";
      if (xPos >= minXPos) {
        xPos--;
      }
      break;

    case 39 /* right arrow */:
      keyPressed = "right ";
      if (xPos <= maxXPos) {
        xPos++;
      }
      break;

    case 38 /* up arrow  */:
      keyPressed = "up";
      if (yPos >= minYPos) {
        yPos--;
      }
      break;

    case 40 /* down arrow */:
      keyPressed = "down";
      if (yPos <= maxYPos) {
        yPos++;
      }
      break;
    default:
      keyPressed = String.fromCharCode(e.keyCode);
  }

  /* keep the ghost within the game play area */
  if (xPos < 0) {
    xPos = 0;
  }
  if (yPos < 0) {
    yPos = 0;
  }

  /* move the ghost to its new position */
  setLeft("ghost", 5 * xPos);
  setTop("ghost", 5 * yPos);

  /* display new position in the header area*/
  document.getElementById("xPos").innerHTML = xPos;
  document.getElementById("yPos").innerHTML = yPos;

  /* display the key user pressed */
  document.getElementById("outputCode").innerHTML = e.keyCode;
  document.getElementById("outputKey").innerHTML = keyPressed;
} /* end of function definition */

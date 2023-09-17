function handleKeys(e) {
  /* event Listener for keydown returns 'e' which has a keycode attached.
       using that keycode, it's possible to know which key was pressed.
       Here we are interested only in arrow keys.             */
  switch (e.keyCode) {
    case 32 /* space bar */:
      keyPressed = "space";
      break;

    case 37 /* left arrow */:
      keyPressed = "left";
      if (xPos > minXPos) {
        xPos--;
      }
      break;

    case 39 /* right arrow */:
      keyPressed = "right ";
      if (xPos < maxXPos) {
        xPos++;
      }
      break;

    case 38 /* up arrow  */:
      keyPressed = "up";
      if (yPos < maxYPos) {
        yPos++;
      }
      break;

    case 40 /* down arrow */:
      keyPressed = "down";
      if (yPos > minYPos) {
        yPos--;
      }
      break;
    default:
      keyPressed = String.fromCharCode(e.keyCode);
  }

  document.getElementById("outputCode").innerHTML = e.keyCode;
  document.getElementById("output").innerHTML = keyPressed;
  document.getElementById("boyWalkingRight").innerHTML = xPos;
  document.getElementById("boyWalkingRight").innerHTML = yPos;
}

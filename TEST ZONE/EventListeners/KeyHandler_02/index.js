/* key handler for arrow keys and space-bar */

let keyPressed = "";
function handleKeys(e) {
  switch (e.keyCode) {
    case 32:
      keyPressed = "space";
      break;
    case 37:
      keyPressed = "left";
      break;
    case 38:
      keyPressed = "up";
      break;
    case 39:
      keyPressed = "right ";
      break;
    case 40:
      keyPressed = "down";
      break;
    default:
      keyPressed = String.fromCharCode(e.keyCode);
  }

  document.getElementById("outputCode").innerHTML += e.keyCode;
  document.getElementById("output").innerHTML += keyPressed;
}

/* this will be key handler for generic input */

function handleKeys(e) {
  let keyPressed = e.keyCode;
  document.getElementById("output").innerHTML = keyPressed;
}

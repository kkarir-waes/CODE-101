/* this will be key handler for generic input */

function handleKeys(e) {
  let keyPressed = String.fromCharCode(e.keyCode);
  document.getElementById("outputCode").innerHTML += e.keyCode;
  document.getElementById("output").innerHTML += keyPressed;
}

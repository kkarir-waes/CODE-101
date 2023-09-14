/* Code to open new window for starting a new games */

let newWindow;

function openWindow(gameName) {
  newWindow = window.open(
    gameName,
    "_blank",
    "top=500,left=500,width=1000,height=1000"
  );

  trimmedName = gameName
    .slice(gameName.indexOf("_") + 1, gameName.indexOf("/"))
    .toUpperCase();
  document.getElementById("status").innerHTML =
    "<h1>Playing " + trimmedName + "</h1>";
}

function closeWindow() {
  document.getElementById("status").innerHTML = "<h1>Thanks for playing</h1>";
  newWindow.close();
}

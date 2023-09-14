/* Global Var */

function grid() {
  var gridHeight = 10;
  var gridWidth = 10;
  var divSize = 50;

  var divId = 0;
  /* set the horizontal position of the character */
  function setLeft(id, x) {
    document.getElementById(id).style.left = x + "px";
  }

  /* set the vertical position of the character */
  function setTop(id, y) {
    document.getElementById(id).style.top = y + "px";
  }

  for (var x = 1; x <= gridWidth; x++) {
    for (var y = 1; y <= gridHeight; y++) {
      /* make a new <div> and apend it to grid <div> */
      var newOb = document.createElement("div");
      document.getElementById("grid").appendChild(newOb);

      divId++;
      newOb.setAttribute("id", divId);
      document.getElementById(divId).innerHTML = ":)";

      setLeft(divId, 50 * x);
      setTop(divId, 50 * y);
      newOb.removeAttribute("id", "");
    }
  }
}

/* make the grid */
grid();

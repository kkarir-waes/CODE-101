/* Javascript for Maze Runner Game */

var mazeData = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 1, 1, 1],
  [1, 0, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1],
];

var px = 0,
  py = 1;

function setLeft(id, x) {
  document.getElementById(id).style.left = x + "px";
}

function setTop(id, y) {
  document.getElementById(id).style.top = y + "px";
}

function drawMaze() {
  for (var y = 0; y < 7; y++) {
    for (var x = 0; x < 8; x++) {
      var newOb = document.createElement("div");
      document.getElementById("maze").appendChild(newOb);

      var divId = Math.random();
      newOb.setAttribute("id", divId);

      if (mazeData[y][x] == 0) {
        document.getElementById(divId).style.backgroundColor = "blue";
      }

      setLeft(divId, 50 * x);
      setTop(divId, 50 * y);
    }
  }
}

function handleArrowKeys(e) {
  if (e.keyCode == 37 && mazeData[py][px - 1] == 0) {
    px--;
  }

  if (e.keyCode == 39 && mazeData[py][px + 1] == 0) {
    px++;
  }

  if (e.keyCode == 38 && mazeData[py - 1][px] == 0) {
    py--;
  }
  if (e.keyCode == 40 && mazeData[py + 1][px] == 0) {
    py++;
  }

  setLeft("ghost", 50 * px);
  setTop("ghost", 50 * py);

  if (px == 7 && py == 5) {
    alert("well done");
  }

  /* display new position in the header area*/
  document.getElementById("xPos").innerHTML = px;
  document.getElementById("yPos").innerHTML = py;
}

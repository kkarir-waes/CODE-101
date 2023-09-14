/* Array to hold the randomly generated 10 picture cards */
var cardDeck = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

/* Array of PictureCards with : card name, img_src file, number_of_times_used */
var pictureCards = [
  ["cow", "cow.jpg", 0],
  ["chicken", "chicken.jpg", 0],
  ["cat", "cat.jpg", 0],
  ["dog", "dog.jpg", 0],
  ["duck", "duck.jpg", 0],
  ["goat", "goat.jpg", 0],
  ["pig", "pig.jpg", 0],
  ["sheep", "sheep.jpg", 0],
];

var imageDirectoryPath = "assets/images/";

function makeCardGrid() {
  let cardName = 0;
  let cardSrcFile = 1;
  let cardTimesUsed = 2;

  for (let x = 0; x < cardDeck.length; x++) {
    /* find a random card that hasn't been chosen more than twice */
    let randomCard = Math.floor(Math.random() * pictureCards.length);

    document.write(
      "<p>BEFORE",
      pictureCards[randomCard][cardName],
      pictureCards[randomCard][cardTimesUsed],
      "</p>"
    );

    if (pictureCards[randomCard][cardTimesUsed] < 2) {
      cardDeck[x] = pictureCards[randomCard][cardName];
      pictureCards[randomCard][cardTimesUsed]++;

      document.write(
        "<p>AFTER:",
        pictureCards[randomCard][cardName],
        pictureCards[randomCard][cardTimesUsed],
        "</p>"
      );

      var newCard = document.createElement("img");

      document.getElementById("grid").appendChild(newCard);
      newCard.setAttribute(
        "src",
        imageDirectoryPath + pictureCards[randomCard][cardSrcFile]
      );
    }
  }
  document.getElementById("cardDisplayArea").innerHTML = cardDeck;
  document.getElementById("pictureCards").innerHTML = pictureCards;
}

makeCardGrid();

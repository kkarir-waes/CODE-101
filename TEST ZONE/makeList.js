/* makeList : Make a html list using an array passed to a function */

function makeList(arguments) {
  let numberedList = "<ol>";
  for (let i = 0; i < arguments.length; i++) {
    numberedList += "<li>" + arguments[i] + "</li>";
  }

  numberedList += "<ol>";
  return numberedList;
}

myList = ["apple", "banana", "cabbage", "pineapple", "orange"];

<div>
  <div>
    <h2>amfkal adls </h2>
    <h3>kdsfk lam ad s</h3>
    <div>
      <h3>dlfdls l</h3>
    </div>
  </div>
</div>;
document.getElementById("demo").innerHTML = makeList(myList);

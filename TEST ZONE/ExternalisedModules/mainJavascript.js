import { myArray } from "./arrayData.js"; /* get the externally defined data array */

for (let x in myArray) {
  let newLI = document.createElement("li"); /* create a new <li> element */
  let textnode = document.createTextNode(
    myArray[x]
  ); /* create the inner HTML text for new <li> */
  newLI.appendChild(textnode); /* attach the text to the new LI */
  document
    .getElementById("URLList")
    .appendChild(newLI); /* finally, attach the LI to the list in the HTML */
}

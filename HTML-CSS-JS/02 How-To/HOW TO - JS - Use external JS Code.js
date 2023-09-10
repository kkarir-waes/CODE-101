// This code is called from with HTML. //
// It creates some HTML H1, H2 and P tags to display on the web page

// A better way is to manipulate the DOM but this is ok for here //

// First, lets add some style to our headings //
window.document.write("<style>");
window.document.write("h1 {color:green;} ");
window.document.write("h2 {color:yellow;}");
window.document.write("#external {background-color:lightblue;}");
window.document.write("</style>");

// now, lets write the HTML code to dispaly something on the web page
window.document.write("<h1>Hello from JavaScript!</h1>");
window.document.write(
  "<h2>This heading is generated by external JavaScript</h2>"
);

window.document.write(
  "<p>This paragraph is also generated by JavaScript code.</p>"
);

window.document.write(
  "<p>This page's title is :<strong>" + document.title + "<strong></p>"
);
window.document.write(
  "<p>The HTML page was last modified:<strong> " +
    document.lastModified +
    "</strong></p>"
);

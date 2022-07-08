/**
 * Template Name: WeBuild - v4.6.1
 * Template URL: https://bootstrapmade.com/free-bootstrap-coming-soon-template-countdwon/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */

var body = document.querySelector("body");
body.addEventListener("click", clickEvent);

function clickEvent(e) {
  var target = e.target;
  if (target != e.currentTarget.querySelector(".searched-list")) {
    var sl = document.querySelector(".searched-list");
    sl.style.display = "none";
  }
  return;
}

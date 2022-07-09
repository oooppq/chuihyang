var body = document.querySelector("body");
body.addEventListener("click", clickEvent);

function clickEvent(e) {
  var target = e.target;
  if (target != e.currentTarget.querySelector(".searched-list")) {
    var sl = document.querySelector(".searched-list");
    if (sl) {
      sl.style.display = "none";
    }
  }
  return;
}

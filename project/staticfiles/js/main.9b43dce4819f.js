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
// 왜 timeout으로 새로 로딩하면 focus가 안될까???
// var form = document.getElementById("searchbox-form");
// var input = document.getElementById("searchbox");
// console.log(input["defaultValue"]);

// function test() {
//   form.submit();
//   input.focus();
//   document.getElementById("searchbox").focus();
// }

// input.addEventListener(
//   "focus",
//   () => {
//     setTimeout(() => {
//       test();
//     }, 1000);
//   },
//   true
// );

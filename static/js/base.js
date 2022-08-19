let windowWidth = document.querySelector(".window-width");
windowWidth.value = window.innerWidth;

var body = document.querySelector("body");
body.addEventListener("click", clickEvent);

function clickEvent(e) {
  var target = e.target;
  if (target != e.currentTarget.querySelector(".searched-list")) {
    var sl = document.querySelector(".searched-list");
    if (sl) {
      sl.classList.remove("d-flex");
      sl.style.display = "none";
    }
  }
  return;
}

$("#searchbox").on("propertychange change keyup paste", function () {
  const value = $(this).val();
  $.ajax({
    url: "../search",
    type: "GET",
    data: {
      searched: value,
    },
    datatype: "json",
    success: function (data) {
      lastList = document.querySelector(".searched-list");
      if (lastList) lastList.remove();
      var outerDiv = document.createElement("div");
      outerDiv.style.color = "black";
      outerDiv.classList.add("searched-list", "d-flex", "flex-column");

      for (let p of data["searchedList"]) {
        let innerDiv = document.createElement("div");
        innerDiv.classList.add("d-flex", "searched-component", "ps-3");
        let emptyDiv = document.createElement("div");
        emptyDiv.classList.add("empty-component");
        emptyDiv.innerHTML = "empty";
        let link = document.createElement("a");
        link.href = "/perfumes/" + p[0];
        link.innerHTML = p[1];
        link.style.width = "80%";
        link.style.textAlign = "left";
        innerDiv.appendChild(emptyDiv);
        innerDiv.appendChild(link);
        outerDiv.appendChild(innerDiv);
      }
      console.log(window.innerWidth);
      if (window.innerWidth > 820) {
        console.log("check1");
        document.querySelector(".search-result-div").appendChild(outerDiv);
      } else {
        console.log("check2");
        document.querySelector("#header").appendChild(outerDiv);
      }
    },
  });
});

$("#mobile-searchbox").on("propertychange change keyup paste", function () {
  const value = $(this).val();
  $.ajax({
    url: "../search",
    type: "GET",
    data: {
      searched: value,
    },
    datatype: "json",
    success: function (data) {
      lastList = document.querySelector(".searched-list");
      if (lastList) lastList.remove();
      var outerDiv = document.createElement("div");
      outerDiv.style.color = "black";
      outerDiv.classList.add("searched-list", "d-flex", "flex-column");

      for (let p of data["searchedList"]) {
        let innerDiv = document.createElement("div");
        innerDiv.classList.add("d-flex", "searched-component", "ps-3");
        let emptyDiv = document.createElement("div");
        emptyDiv.classList.add("empty-component");
        emptyDiv.innerHTML = "empty";
        let link = document.createElement("a");
        link.href = "/perfumes/" + p[0];
        link.innerHTML = p[1];
        link.style.width = "80%";
        link.style.textAlign = "left";
        innerDiv.appendChild(emptyDiv);
        innerDiv.appendChild(link);
        outerDiv.appendChild(innerDiv);
      }
      document.querySelector("#header").appendChild(outerDiv);
    },
  });
});

let index = 0;
let rankingLists = document.querySelectorAll(".ranking-list");

function borderHighlight(rankingList) {
  rankingList
    .querySelectorAll("li")
    [(index + 9) % 10].classList.remove("selected");
  rankingList.querySelectorAll("li")[index].classList.add("selected");
}

function interval() {
  setInterval(function () {
    for (rankingList of rankingLists) {
      borderHighlight(rankingList);
    }

    index = (index + 1) % 10;
  }, 2000);
}

interval();

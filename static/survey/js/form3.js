var num = 1;
var choice = 0;
var q = {
  1: {
    title:
      "평소에 즐겨 입는 옷 스타일을 골라주세요.",
    A: "꾸안꾸",
    B: "오피스룩",
    C: "스트릿",
    D: "츄리닝"
  },
  2: {
    title:
      "자주 듣는 얼굴상을 골라주세요.",
    A: "강아지상",
    B: "고양이상",
    C: "물고기상",
    D: "여우상"
  },
  3: {
    title:
      "아래 보기 중 가장 신경 쓰는 장신구를 골라주세요.",
    A: "귀걸이",
    B: "시계",
    C: "목걸이",
    D: "가방"
  },
  4: {
    title:
      "자신의 이미지와 유사한 계절을 골라주세요.",
    A: "봄",
    B: "여름",
    C: "가을",
    D: "겨울"
  },
  5: {
    title:
      "자신의 헤어스타일을 골라주세요.",
    A: "단발머리",
    B: "긴머리",
    C: "염색머리",
    D: "웨이브"

  },
  6: {
    title:
      "자신을 한마디로 설명할 수 있는 단어를 골라주세요",
    A: "큐티",
    B: "섹시",
    C: "청순",
    D: "도도"

  },


};
var mq = {
  1: {
    title:
      "평소에 즐겨 입는 옷 스타일을 골라주세요.",
    A: "꾸안꾸",
    B: "오피스룩",
    C: "스트릿",
    D: "츄리닝"
  },
  2: {
    title:
      "자주 듣는 얼굴상을 골라주세요.",
    A: "강아지상",
    B: "고양이상",
    C: "공룡상",
    D: "여우상"
  },
  3: {
    title:
      "아래 보기 중 가장 신경 쓰는 장신구를 골라주세요.",
    A: "가방",
    B: "시계",
    C: "목걸이/귀걸이",
    D: "벨트"
  },
  4: {
    title:
      "자신의 이미지와 유사한 계절을 골라주세요.",
    A: "봄",
    B: "여름",
    C: "가을",
    D: "겨울"
  }, 5: {
    title:
      "자신의 헤어스타일을 골라주세요.",
    A: "덮은머리",
    B: "올린머리",
    C: "장발",
    D: "짧은머리"

  },
  6: {
    title:
      "자신을 한마디로 설명할 수 있는 단어를 골라주세요",
    A: "큐티",
    B: "남성적",
    C: "도도",
    D: "섹시"
  },


};

function startW() {
  choice = 1;
  next();
}
function startM() {
  choice = 2;
  next();
}
$("#A").click(function () {
  var preValue = $("#rA").val();
  $("#rA").val(parseInt(preValue) + 1);
  console.log($("#rA").val());
  next();
});
$("#B").click(function () {
  var preValue = $("#rB").val();
  $("#rB").val(parseInt(preValue) + 1);
  next();
});
$("#C").click(function () {
  var preValue = $("#rC").val();
  $("#rC").val(parseInt(preValue) + 1);
  next();
});
$("#D").click(function () {
  var preValue = $("#rD").val();
  $("#rD").val(parseInt(preValue) + 1);
  next();
});
function pageTurn() {
  location.replace("/survey/result3/");

}
function next() {
  if (num == 6) {

    $(".question").hide();
    $(".process").show();
    setTimeout(pageTurn, 3000);



    let idx = 0;
    let final = 0;
    let resultnum = [$("#rA").val(), $("#rB").val(), $("#rC").val(), $("#rD").val()];
    for (let i = 0; i < 4; i++) {
      if (resultnum[i] >= idx) {
        idx = resultnum[i];
        final = i;
      }
    }

    if (final == 0) {
      if (choice == 1)
        localStorage.setItem("finalscent", "WA");
      else localStorage.setItem("finalscent", "MA");
    }
    else if (final == 1) {
      if (choice == 1)
        localStorage.setItem("finalscent", "WB");
      else localStorage.setItem("finalscent", "MB");

    }
    else if (final == 2) {
      if (choice == 1)
        localStorage.setItem("finalscent", "WC");
      else localStorage.setItem("finalscent", "MC");
    }
    else {
      if (choice == 1)
        localStorage.setItem("finalscent", "WD");
      else localStorage.setItem("finalscent", "MD");
    }
    console.log(localStorage.finalscent);


  } else {
    $(".sex").hide();
    $(".question").show();

    $(".progress-bar").attr("style", "width: calc(100/6*" + num + "%)");
    if (choice == 1) {
      $("#title").html(q[num]["title"]);
      $("#A").html(q[num]["A"]);
      $("#B").html(q[num]["B"]);
      $("#C").html(q[num]["C"]);
      $("#D").html(q[num]["D"]);
      num++;
    }
    else if (choice == 2) {
      $("#title").html(mq[num]["title"]);
      $("#A").html(mq[num]["A"]);
      $("#B").html(mq[num]["B"]);
      $("#C").html(mq[num]["C"]);
      $("#D").html(mq[num]["D"]);
      num++;
    }



  }
}



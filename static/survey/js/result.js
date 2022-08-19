var mbti_result=document.getElementById("mbti");
var img_result=document.getElementById("show");
var explain_result=document.getElementsByClassName("words")[0];

mbti_result.innerText=localStorage.getItem('mbti');
img_result.setAttribute('src','/static/survey/img/'+localStorage.getItem('img'));
explain_result.innerText=localStorage.getItem('explain');

var designate={
  0:{
    EN:'딥디크-오데썽',
    ES:'에르메스-운자르뎅수르닐',
    IN:'조르지오아르마니-떼울롱',
    IS:'조말론-다크앰버앤진저릴리',
  },
  1:{
    NT:'산타마리아노벨라-알바디서울',
    NF:'바이레도-블랑쉬',
    ST:'톰포드-블랙오키드',
    SF:'아쿠아디파르마-매그놀리아',
  },
  2:{
    TP:'크리드-실버마운틴워터',
    TJ:'르라보-떼누아',
    FP:'메종마르지엘라-레이지선데이모닝',
    FJ:'메모파리-인레',
  }
}
//h
function parse_change(){
  var str=localStorage.getItem('mbti');

  for(var i=0; i<3;i++){
    var comb=designate[i][str.substring(i,i+2)];
    var pf_name=document.getElementsByClassName("caption")[i];
    var pf_img=document.getElementsByClassName("pf_img")[i];
    pf_name.innerText=comb;
    pf_img.setAttribute('src','/static/survey/img/'+comb+'.png');
  }
}
parse_change();


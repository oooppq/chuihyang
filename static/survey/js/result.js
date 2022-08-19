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
    IN:'르라보-떼누아',
    IS:'조말론-다크앰버앤진저릴리',
  },
  1:{
    NT:'메종마르지엘라-소울오브더포레스트',
    NF:'바이레도-블랑쉬',
    ST:'톰포드-블랙오키드',
    SF:'크리드-실버마운틴워터',
  },
  2:{
    TP:'크리드-실버마운틴워터',
    TJ:'르라보-떼누아',
    FP:'메종마르지엘라-소울오브더포레스트',
    FJ:'샤넬-드블루',
  }
}
var designate_num={
  0:{
    EN:35808,
    ES:7572,
    IN:1973,
    IS:6395,
  },
  1:{
    NT:11519,
    NF:19209,
    ST:61876,
    SF:18763,
  },
  2:{
    TP:18763,
    TJ:1973,
    FP:11519,
    FJ:2283,
  }
}

function parse_change(){
  var str=localStorage.getItem('mbti');

  for(var i=0; i<3;i++){
    var comb=designate[i][str.substring(i,i+2)];
    var comb_num=designate_num[i][str.substring(i,i+2)];
    var pf_name=document.getElementsByClassName("caption")[i];
    var pf_img=document.getElementsByClassName("pf_img")[i];
    var pf_num=document.getElementsByClassName("info_link")[i];
  
    localStorage.setItem('pf_f',pf_num);
    pf_name.innerText=comb;
    pf_num.setAttribute('href','/perfumes/'+comb_num);
    pf_img.setAttribute('src','/static/survey/img/'+comb+'.png');
  }
}
parse_change();


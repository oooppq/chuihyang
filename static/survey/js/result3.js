
//$("#scent").html(localStorage.finalscent + " type");

//console.log(resultscent);


var result = {
    WA: {
        explain:
            "화려함보다는 수수함을 선호하는 당신, 진한 화장보다는 액세서리 하나로 포인트를 주는 것을 좋아하는 타입이에요. 튀는 스타일보다는 면 티와 슬렉스 조합을 자주 찾으시죠?? 은은하게 스며드는 당신의 매력에 정신을 못 차리겠네요~",
        img: "WA.jpg",
    },
    WB: {
        explain:
            "어딜 가나 시선집중!! 당신의 도도함에 끌리지 않는 이성 찾기란 한양에서 김서방 찾기~~^^ 깔끔하면서 세련된 스타일을 선호하는 타입이에요.",
        img: "WB.jpg",
    },
    WC: {
        explain:
            "밝고 통통 튀는 이미지를 갖고 있으시네요. 어떤 스타일도 잘 소화해 내는 당신이기에 평소 스타일의 정반대인 오피스룩을 도전해 보는 걸 추천해 드려요. 팔색조 매력의 당신의 변신을 응원합니다~",
        img: "WC.jpg",
    },
    WD: {
        explain:
            "자신만의 확고한 스타일이 있으시군요. 남들은 쉽게 도전하지 못하는 스타일도 누구보다 찰떡같이 소화하는 당신~ 고가의 브랜드 의상을 즐겨 입으시네요. 세련되면서 고혹한 이미지.. 정말 부럽습니다!",
        img: "WD.jpg",
    },
    MA: {
        explain:
            "화려함보다는 수수함을 선호하는 당신, 튀는 의상보다는 액세서리 하나로 포인트를 주는 것을 좋아하는 타입이에요. 가벼운 면 티와 슬렉스 조합을 자주 입으시죠?? 은은하게 스며드는 당신의 매력에 정신을 못 차리겠네요~",
        img: "MA.jpg",
    },
    MB: {
        explain:
            "어딜 가나 시선집중!! 당신의 도도함에 끌리지 않는 이성 찾기란 한양에서 김서방 찾기~~^^ 깔끔하면서 세련된 스타일을 선호하는 타입이에요.",
        img: "MB.jpg",
    },
    MC: {
        explain:
            "밝고 통통 튀는 이미지를 갖고 있으시네요. 어떤 스타일도 잘 소화해 내는 당신이기에 평소 스타일의 정반대인 오피스룩을 도전해 보는 걸 추천해 드려요. 팔색조 매력의 당신의 변신을 응원합니다~",
        img: "MC.jpg",
    },
    MD: {
        explain:
            "자신만의 확고한 스타일이 있으시군요. 남들은 쉽게 도전하지 못하는 스타일도 누구보다 찰떡같이 소화하는 당신~ 고가의 브랜드 의상을 즐겨 입으시네요. 세련되면서 고혹한 이미지.. 정말 부럽습니다!",
        img: "MD.jpg",
    },

};

var resultscent = localStorage.getItem('finalscent');
$("#img").attr("src", "/static/survey/img/" + result[resultscent]["img"]);
$("#scent").html(resultscent + " type");
$("#explain").html(result[resultscent]["explain"]);

var designate={
   
      WA:['딥디크-오데썽','에르메스-운자르뎅수르닐','르라보-떼누아'],
      WB:['에르메스-운자르뎅수르닐','르라보-떼누아','조말론-다크앰버앤진저릴리'],
      WC:['르라보-떼누아','조말론-다크앰버앤진저릴리','톰포드-블랙오키드'],
      WD:['조말론-다크앰버앤진저릴리','톰포드-블랙오키드','바이레도-블랑쉬'],
    
      MA:['톰포드-블랙오키드','바이레도-블랑쉬','크리드-실버마운틴워터'],
      MB:['바이레도-블랑쉬','크리드-실버마운틴워터','샤넬-드블루'],
      MC:['크리드-실버마운틴워터','샤넬-드블루','메종마르지엘라-소울오브더포레스트'],
      MD:['샤넬-드블루','메종마르지엘라-소울오브더포레스트','딥디크-오데썽']
    
  }
  
  var designate_num={
      WA:[35808,7572,1973],
      WB:[7572,1973,6395],
      WC:[1311,6395,61876],
      WD:[6395,61876,19209],
    
      MA:[61876,19209,18763],
      MB:[19209,18763,2283],
      MC:[18763,2283,11519],
      MD:[2283,11519,35808]
  }

  function change(){
    var str=localStorage.getItem('finalscent');
    

    for(var i=0; i<3;i++){
      var comb=designate[str][i];
      var comb_num=designate_num[str][i];
      var pf_name=document.getElementsByClassName("caption")[i];
      var pf_img=document.getElementsByClassName("pf_img")[i];
      var pf_num=document.getElementsByClassName("info_link")[i];

      pf_name.innerText=comb;
      pf_num.setAttribute('href','/perfumes/'+comb_num);
      pf_img.setAttribute('src','/static/survey/img/'+comb+'.png');
    }
  }
  change();

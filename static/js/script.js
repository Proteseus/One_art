function Toggle_hamburger_menu() {
    var navElem = document.getElementById("myTopnav");
    if (navElem.className === "topnav") {
      navElem.className += " responsive";
    } else {
      navElem.className = "topnav";
    }
  }

  function FormTrigger(isFocused) {
    var extraBuyerInfo = document.getElementById("companyName");
    if (isFocused == true) {
      extraBuyerInfo.style.display = "flex";
    }
    
    else {
      extraBuyerInfo.style.display = "none";
    }
  }
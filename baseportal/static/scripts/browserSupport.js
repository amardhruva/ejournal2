  if(!(CSS.supports("display","grid") || CSS.supports("grid-template-areas","abc"))){
      window.location.href="browserSupport.html";
      console.log("does not support");
      //alert("does not support");
}else{
    console.log("Supports");
    //alert("Support");
}
function goRightOne(){ // inner stuff slides left
	var initalLeftMargin = $( ".sliderOne" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin - 204); // extra 2 for border
	$( ".sliderOne" ).animate({marginLeft: newLeftMargin}, 500);
}
function goLeftOne(){ // inner stuff slides right
	var initalLeftMargin = $( ".sliderOne" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin + 204); // extra 2 for border
	$( ".sliderOne" ).animate({marginLeft: newLeftMargin}, 500);
}

function goRightTwo(){ // inner stuff slides left
	var initalLeftMargin = $( ".sliderTwo" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin - 204); // extra 2 for border
	$( ".sliderTwo" ).animate({marginLeft: newLeftMargin}, 500);
}
function goLeftTwo(){ // inner stuff slides right
	var initalLeftMargin = $( ".sliderTwo" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin + 204); // extra 2 for border
	$( ".sliderTwo" ).animate({marginLeft: newLeftMargin}, 500);
}

function goRightThree(){ // inner stuff slides left
	var initalLeftMargin = $( ".sliderThree" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin - 204); // extra 2 for border
	$( ".sliderThree" ).animate({marginLeft: newLeftMargin}, 500);
}
function goLeftThree(){ // inner stuff slides right
	var initalLeftMargin = $( ".sliderThree" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin + 204); // extra 2 for border
	$( ".sliderThree" ).animate({marginLeft: newLeftMargin}, 500);
}

function goRightFour(){ // inner stuff slides left
	var initalLeftMargin = $( ".sliderFour" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin - 204); // extra 2 for border
	$( ".sliderFour" ).animate({marginLeft: newLeftMargin}, 500);
}
function goLeftFour(){ // inner stuff slides right
	var initalLeftMargin = $( ".sliderFour" ).css('margin-left').replace("px", "")*1;
	var newLeftMargin = (initalLeftMargin + 204); // extra 2 for border
	$( ".sliderFour" ).animate({marginLeft: newLeftMargin}, 500);
}
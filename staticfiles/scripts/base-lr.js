$(document).ready(function(){
	var _left_box_height = $('#base-lr-primary > .left-box').css("height").replace('px','')*1;
	var _right_box_height = $('#base-lr-primary > .right-box').css("height").replace('px','')*1;
	alert(_left_box_height > _right_box_height);
	if(_left_box_height > _right_box_height){
		$('#base-lr-primary > .right-box').css({"height":_left_box_height});
	}
	else{
		$('#base-lr-primary > .left-box').css({"height":_right_box_height});
	}
});
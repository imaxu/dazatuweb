$(document).ready(function(){
	$("#ext-menu > .menu").tabs();
	$("#tasks-list > .list-wrap").tabs();
	$(".dazatu-list > .add > .headimage").click(function(){
		//
	});
	
	$(".close").click(function(){
		$(this).parent().parent().hide(250);
	});
	
	$(".get-more").click(function(){
		location.href = "/task/list/1/" + $(this).attr("data");
	});
});
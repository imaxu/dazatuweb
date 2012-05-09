$(document).ready(function(){
	$( '.button-login' )
		.click(function(){
			location.href='/user/login/';
		});
	//城市选择overlay对象及属性设置
	var trigger = $("#city-selector").overlay({

		// some mask tweaks suitable for modal dialogs
		mask: {
			color: '#000000',
			loadSpeed: 200,
			opacity: 0.5
		},
		top:'center',
		closeOnClick: false
	});
	//城市选择对话框关闭按钮事件设置
	$(".clsbtn").click(function(e){
		trigger.overlay().close();
	});
	$(".clsbtn").mouseover(function(e){
		this.src = "/static/images/popWinClos_hover.png";
	});
	$(".clsbtn").mouseout(function(e){
		this.src = "/static/images/popWinClos.png";
	});	
	
	$(".region").click(function(){
		_region = this.innerText
		$.ajax({
				url:"/api/users/set__region/",			
				type:'POST',
				data:{	
						'region':_region
					},
				success:function(data,textStatus){
							window.document.getElementById("city-selector").innerText = data + "▼";
						},
				error:function(xmlHttpRequest, textStatus, errorThrown){
				}
		});
		
		trigger.overlay().close();
	});
	$.metadata.setType("attr", "rules");
	/*  change jQuery.ajax setup that ajax can post data */
	$.ajaxSetup({ 
		beforeSend: function(xhr, settings) {
			function getCookie(name) {
			 var cookieValue = null;
				if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
					for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
			 // Only send the token to relative URLs i.e. locally.
			 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		} 
	});		
	/* change jQuery.ajax setup that ajax can post data END */	
	/* init jquery.qtip plugin */
	if($(".qtipitem[title]").qtip != undefined){
		$(".qtipitem[title]").qtip({
			position:{
				my:'bottom center',
				at:'top center'
			},
			style:{
				classes:'ui-tooltip-green ui-tooltip-shadow'
			}
		});	
	}
	/* init jq.qtip plugin END */
});
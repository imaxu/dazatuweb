function ValInput(obj){
	if ( obj.value == '输入您的电子邮箱地址' || obj.value.length == 0 ){
		return false;
	}
	return true;
}
$(document).ready(function(){
	
	$.metadata.setType("attr", "rules");	
	//最近完成的任务 jquery滑动对象及属性设置
	var task_slider = $('#recent-tasks').bxSlider({
		auto:true,
		controls: false,
		mode:'vertical',
		displaySlideQty: 4,
		moveSlideQty: 3	,
		pause: 5000
	});
		//下一组的按钮事件设置
	$('#go-prev').click(function(){	
		task_slider.goToPreviousSlide();
		return false;
	  });
		//上一组的按钮时间设置
	$('#go-next').click(function(){
		task_slider.goToNextSlide();
		return false;
	  });
	  //end
	  
	//打杂兔轮显图片
	var dazatu_slider = $('#reco-dazatu-list').bxSlider({
		auto:true,
		controls: false,
		mode:'fade',
		displaySlideQty: 1,
		moveSlideQty: 1	,
		pause: 7000
	});
	//定义JQ验证对象
	
	//注册输入框初始化设置
	$('#in-usermail').css({color:'#acacac'});
	$('#in-usermail').click(function(e){
		if (!ValInput(this)){
			this.value = '';
			$('#in-usermail').css({color:'#959595'});
		}
	});
	$('#in-usermail').blur(function(e){
		if (!ValInput(this)){
			$('#in-usermail').css({color:'#acacac'});	
			this.value = '输入您的电子邮箱地址';
		}
	});	
	//end	
	var msgbox_overlay = $("#msgbox").overlay({

							// some mask tweaks suitable for modal dialogs
							mask: {
								color: '#000000',
								loadSpeed: 200,
								opacity: 0.5
							},
							top:'20%',
							closeOnClick:false,
							closeOnEsc:false
						});	
	$("#msgbox > .clsbtn")
		.click(function(){
			msgbox_overlay.overlay().close();
		});
	$('#loginform').validate({
						errorPlacement:function(msg,el){
							if(msg.text()){
								$("#msgbox > .content").text(msg.text());
							}
						}
					});			
	//开始 按钮初始化设置
	$('#sub').click(function(e){
		if(true == $('#loginform').validate().element("#in-usermail")){
			$('#v-sub').click();
		}
		else{
			$("#msgbox > .content").html("<div style='width:90%;margin:0 auto;'>我们的打杂兔们喜欢真实的您，希望您填写真实有效的电子邮件地址。</div>");	
			msgbox_overlay.overlay().load();
		}
	});
	
});
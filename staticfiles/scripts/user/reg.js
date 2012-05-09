$(document).ready(function(){
	var __debug__ = true;
	var __curr_step__ = 1;
	var time_in = 500;
	var time_out = 500;
	/* disabled keydown event for tab */
	//$(document).bind("keydown", "tab",function (evt){return false; });
	/* init a overlay obj */
	var loginProcWind = $("#login-proc").overlay({

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
	/* init a overlay obj END */	
	/* set  appellation control  event */
	$( "#appellation" )
		.button()
		.click(function() {
			//
			setAppellationDisable();
		})
		.buttonset();
	$( "#appe-selector-form > ul > li > a")
		.click(function(){
			$("#u_selfname").text($("#u_fname").val());
			$("#u_selappe").text(this.innerText);
			$( '#appellation' )
				.text(this.innerText);
			$("#u_appellation").val(this.innerText);
			$( "#appe-selector-form").hide(time_out);
		});
	/* set  appellation control  event end */
	
	//添加中文姓名验证方法
	$.validator.addMethod(
		"cn_name",
		function(val,el,par){
			var cnReg = /^[\u0391-\uFFE5]+$/;
			return cnReg.test(val);
		},
		"请您输入由中文字符组成的姓名。");
	$.validator.addMethod(
		"cn_idcard",
		function(val,el,par){
			var cnReg = /^[1-9]\d{16}(\d|X)$/;	
			return cnReg.test(val);
		},
		"请您输入真实有效的身份证号码。");	
	$.validator.addMethod(
		"cn_mobile",
		function(val,el,par){
			var cnReg = /^1[3,5]\d{9}$/;
			return cnReg.test(val);
		},
		"请您输入真实有效的手机号码。");	
	$("#user-reg-area").validate({
		errorPlacement:function(msg,el){
			if(msg.text()){
				$("#" + el.attr("id") + "_tip").addClass("errmsg").removeClass("passmsg").text(msg.text());
			}
		}
	});	

	bindInptEvent("#u_email","恭喜您，您输入的电子邮箱可以使用。");
	bindInptEvent("#u_pwd","密码验证通过。");
	bindInptEvent("#u_repwd","");
	bindInptEvent("#u_fname","");
	bindInptEvent("#u_lname","");
	bindInptEvent("#u_appellation","");	
	bindInptEvent("#u_idcard","");	
	bindInptEvent("#u_mphone","");	
	
	function bindInptEvent(elem,onBlurTxt){
		$(elem)
			.blur(function(){
				if($("#user-reg-area").validate().element(elem)){
					$(elem + "_tip").removeClass("errmsg").text(onBlurTxt);
					if(onBlurTxt.length > 0 ){
						$(elem + "_tip").addClass("passmsg");
					}
				}
			})
			.focus(function(){
				$(elem + "_tip").removeClass("errmsg").text($(elem + "_tip").attr("data"));
			});		
	}
	/* init controls of form's validate event end */
	//初始化密码强度验证
	$('#u_pwd').passwordStrength();	
	//初始化元素事件
	$('#go-prev').hide();
	$('#submit-btn').hide();
	//最近完成的任务 jquery滑动对象及属性设置
	var slider = $('#user-reg-area').bxSlider({
		auto:false,
		infiniteLoop: false,
		controls: false,
		hideControlOnEnd: true,
		mode:'horizontal',
		displaySlideQty: 1,
		moveSlideQty: 1,
		onNextSlide:function(currentSlideNumber, totalSlideQty, currentSlideHtmlObject){

				//控制按钮
				if(currentSlideNumber > 0){
					$('#go-prev').show(time_in);
				}
				if(currentSlideNumber == totalSlideQty-1){
					$('#go-next').hide(time_out);
					$('#submit-btn').show(time_in);
				}
				//控制步骤导航
				$('#grp-' + (currentSlideNumber - 1) ).removeClass("curr-step").addClass("not-curr-step").show("slow");
				$('#grp-' + currentSlideNumber).addClass("curr-step").removeClass("not-curr-step").show("slow");
				__curr_step__++;

			},
		onPrevSlide:function(currentSlideNumber, totalSlideQty, currentSlideHtmlObject){
				//控制按钮
				$('#submit-btn').hide(time_out);
				$('#go-next').show(time_in);
				if(currentSlideNumber == 0){
					$('#go-prev').hide(time_out);
				}
				
				//控制步骤导航
				$('#grp-' + (currentSlideNumber + 1) ).removeClass("curr-step").addClass("not-curr-step");
				$('#grp-' + currentSlideNumber).addClass("curr-step").removeClass("not-curr-step");	
				__curr_step__--;
			},
		onLastSlide:function(currentSlideNumber, totalSlideQty, currentSlideHtmlObject){
				$("#step-2").html("");		
				$("#prevfname1").text($("#u_fname").val());
				$("#prevappe").text($("#u_appellation").val());
				$("#prevemail").text($("#u_email").val());
				$("#prevfname2").text($("#u_fname").val());
				$("#prevlname").text($("#u_lname").val());
				$("#previdcard").text($("#u_idcard").val());
				$("#prevmphone").text($("#u_mphone").val());
			}
	});
		//上一步按钮点击事件
	$('#go-prev').click(function(){
		slider.goToPreviousSlide();
		return false;
	  });
		//继续按钮点击事件
	$('#go-next').click(function(){
		if(__curr_step__ == 1){
			var __email__ = $('#user-reg-area').validate().element('#u_email');
			var __password__ = $('#user-reg-area').validate().element('#u_pwd');
			var __repassword__ = $('#user-reg-area').validate().element('#u_repwd');
			if(!__email__ || !__password__ || !__repassword__){
				loginProcWind.overlay().load();
				$("#regresult").html("您需要先填写完基本信息后才可以继续。");
				return false;
			}			
			//validate user email
			loginProcWind.overlay().load();
			$("#regresult").html("正在验证您的电子邮件地址，请您稍等。");	
			$.ajax({
				url:"/user/reg/validate/",
				type:'POST',
				data:{
						'email':$("#u_email").val()
				},
				success:function(data,textStatus){
					if('1' == data){
						loginProcWind.overlay().close();					
						slider.goToNextSlide();
					}
					else{
						$("#regresult").html(data);
						
					}							
				},
				error:function(xmlHttpRequest, textStatus, errorThrown){
					$("#regresult").html("<div>验证电子邮件时发生了不可预料的错误。" + errorThrown + "</div>");
				}
			});			

			return false;
		}
		if(__curr_step__ == 2){
			var __fname__ = $('#user-reg-area').validate().element('#u_fname');
			var __lname__ = $('#user-reg-area').validate().element('#u_lname');
			var __appellation__ = $('#user-reg-area').validate().element('#u_appellation');
			var __idcard__ = $('#user-reg-area').validate().element('#u_idcard');	
			var __mphone__ = $('#user-reg-area').validate().element('#u_mphone');
			if(!__fname__ || !__lname__ || !__appellation__ || !__idcard__ || !__mphone__){
				loginProcWind.overlay().load();
				$("#regresult").html("您需要先填写完实名信息后才可以继续。");
				return false;
			}
			//加入服务器端验证
			loginProcWind.overlay().load();
			$("#regresult").html("正在验证您的身份证号码和手机号码，请您稍等。");	
			$.ajax({
				url:"/user/reg/validate/",
				type:'POST',
				data:{
						'idcard':$("#u_idcard").val(),
						'mphone':$("#u_mphone").val(),
				},
				success:function(data,textStatus){
					if('1' == data){
						loginProcWind.overlay().close();					
						slider.goToNextSlide();
					}
					else{
						$("#regresult").html(data);
						
					}							
				},
				error:function(xmlHttpRequest, textStatus, errorThrown){
					$("#regresult").html("<div>验证电子邮件时发生了不可预料的错误。" + errorThrown + "</div>");
				}
			});				
			return false;
		}

	  });


	$( '#submit-btn' ).click(function(){
		loginProcWind.overlay().load();
		$("#regresult").html("正在向服务器提交注册申请，视网络状况可能要稍等片刻。");
		$.ajax({
			url:"/user/reg/post/",			
			type:'POST',
			data:{
					'fname':$("#u_fname").val(),
					'lname':$("#u_lname").val(),
					'appe':$("#u_appellation").val(),
					'email':$("#u_email").val(),
					'password':$("#u_pwd").val(),
					'idcard':$("#u_idcard").val(),
					'mphone':$("#u_mphone").val()
				},
			success:function(data,textStatus){
						
						$("#login-proc > .clsbtn").click(function(){
								var u_id = $(data).filter("#reg_success").attr("data");
								if(u_id){
									location.href="/user/center/"// + u_id;							
								}
						});			
						$("#regresult").html(data);
					},
			error:function(xmlHttpRequest, textStatus, errorThrown){
				$("#regresult").html("<div>读取数据时发生不可预料的错误。" + errorThrown + "</div>");
			}
		});
	});
	//对话框关闭按钮事件设置
	$(".clsbtn").click(function(e){
		loginProcWind.overlay().close();
	});	
	//根据当前状态决定称谓候选列表是否显示
	function setAppellationDisable(){
		var _obj = $( "#appellation" );
		var _targetObj = $('#appe-selector-form');
		if( _targetObj.css('display') == 'none'){
			var _top = _obj.offset().top;
			var _left = _obj.offset().left;
			var _height = _obj.height();
			_targetObj
				.css({
					'position':'absolute',
					'top': (_top + _height) + 'px',
					'left':_left + 'px'
				}).show(time_in);
		}
		else{
			_targetObj.hide(time_out);
		}
	}
	
	function ValidateElement(element){
		
	}
});


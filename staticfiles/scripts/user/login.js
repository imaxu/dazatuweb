$(document).ready(function(){
	$("#loginbtn").click(function(){
		$("#loginform").validate({
			errorPlacement:function(errmsg,el){
				$("#errs").html(errmsg);
			}
		});
		if($("#loginform").validate().form()){
			$.ajax({
				url:"/user/login/validate/",
				type:'POST',
				data:{
						'l_account':$("#l_account").val(),
						'l_password':$("#l_password").val(),
						'l_session_remember_me_input':getCheckBoxVal()
				},
				success:function(data,textStatus){
					if(/^\d*$/.test(data)){
						location.href="/user/center/";
					}
					else{
						$("#errs").html(data);
					}							
				},
				error:function(xmlHttpRequest, textStatus, errorThrown){
					$("#errs").html("<div>登陆时发生了不可预料的错误。" + errorThrown + "</div>");
				}
			});
			return false;
		}
		return false;
	});
	
	function getCheckBoxVal(){
		return !($("#l_session_remember_me_input").attr("checked") == undefined);
	}
});
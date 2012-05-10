$(document).ready(function(){
	//bind event:add a private
	$(".add-private-msg").click(function(){
		if($(".private-msg").css("display")=="none"){
			$(".private-msg").show(250);
			return;
		}
		$(".private-msg").hide(250);
	});

	//add a new location
	$(".add-a-location").click(function(){
		$(".locations > .location:last-child")
			.after(
				$(".location-template").html()
			);
		bind_del_location_event();
	});

	$(".go-to-next").click(function(){

		var $needVehicle = $("#need_vehicle")[0].checked;
		var $doneWithVirtual = $("#done_with_virtual")[0].checked;

		$("input[name='need_vehicle']").val($needVehicle);
		$("input[name='done_with_virtual']").val($doneWithVirtual);

		$("#go-to-next").click();
	});
	
	$(".opt-change-deadline").click(function(){
		$(this).hide();
		$(".opt-deadline").show(250);
		
	});
	/* init a overlay obj */
	var trigger = $("#pre-post").overlay({

		// some mask tweaks suitable for modal dialogs
		mask: {
			color: '#000000',
			loadSpeed: 200,
			opacity: 0.5
		},
		top:'20%',
		closeOnClick:false,
		closeOnEsc:true
	});	
	/* init a overlay obj END */
	
	//bind event:close the overlay when click the closebutton
	$(".clsbtn").click(function(e){
		trigger.overlay().close();
	});	
	$(".opt-change-task-tip").click(function(){
		call_task_base_settings();
	});
	//bind event : remove location
	function bind_del_location_event(){
		//event:remove a location
		$(".remove-link").click(function(){
			del_location_from_removelink(this);
		});
	}
	//del a location
	function del_location_from_removelink(removelink){
		if($(".locations").children().length>1){
			_n = $(removelink)
					.parent()
						.parent()
							.parent();
			_n.hide(250);
			_n.remove();
		}
	}
	function call_task_base_settings(){
		$.ajax({
				url:"/task/post/widget/",			
				type:'POST',
				data:{
						'widget_name':'step1',
						'task_type':$("input[name='task_type']").val(),
						'task_repeat_frequency':$("input[name='task-repeat-frequency']").val(),
						'task_assign_model':$("input[name='task-assign-model']").val()
						
					},
				success:function(data,textStatus){
							$("#dialog-content").html(data);
						},
				error:function(xmlHttpRequest, textStatus, errorThrown){
					$("#dialog-content").html("<div>加载页面内容时发生了不可预料的错误。" + errorThrown + "</div>");
				}
		});
		trigger.overlay().load();	
	}
	//**************  render part  *******************************************
	//render a  location 
	$(".locations").append($(".location-template").html());
	bind_del_location_event();	
	//option deadline
	$(".opt-change-deadline").text($("#finished_deadline").val());	
	if($("#is_postback").val() == "False"){
		call_task_base_settings();
	}
});

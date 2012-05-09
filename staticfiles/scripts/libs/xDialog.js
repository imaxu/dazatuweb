function xDialog(triggerSourceObject,path){
		this.overlay = $(triggerSourceObject).overlay({

							// some mask tweaks suitable for modal dialogs
							mask: {
								color: '#000',
								loadSpeed: 200,
								opacity: 0.5
							},
							top:'center',
							closeOnClick: false
						});
		$(".dialog > .clsbtn").mouseover(function(e){
			this.src = path + "/images/popWinClos_hover.png";
		});
		$(".dialog > .clsbtn").mouseout(function(e){
			this.src = path + "/images/popWinClos.png";
		});	
		this.load = function(){
			
			this.overlay.load();
			};		
	}
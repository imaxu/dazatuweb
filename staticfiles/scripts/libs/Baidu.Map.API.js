
// 编写自定义函数,创建标注
function addMarker(point, index,icon1,icon2,icon3){

   var opts = {
    width : 220,     // 信息窗口宽度
    height: 60,     // 信息窗口高度
    title : ""  // 信息窗口标题
  }
  var infoWindow = new BMap.InfoWindow("这是一个任务", opts);  // 创建信息窗口对象  
  var marker = new BMap.Marker(point, {icon: icon1});
  map.addOverlay(marker);
  marker.addEventListener("click",function(){
		this.openInfoWindow(infoWindow);
		this.setIcon(icon2);
		});	
  marker.addEventListener("mouseover",function(){
		this.setIcon(icon3);	
		});
  marker.addEventListener("mouseout",function(){
		this.setIcon(icon1);
		});		
}
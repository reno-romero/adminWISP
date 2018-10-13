$(document).ready(function(){
	$("li a").click(function(){
		var seccion = $(this).attr("id");
		
		if (seccion=="menu-servicios")
		{
			$("nav#nav-servicios").show();
		} 
	});

	$("nav#nav-servicios ul li").click(function(){
		var servicio = $(this).attr("class");

		if (servicio=="icon-internet")
		{
			borrarServicios();
			$("article#internet").show();
		} 
		if (servicio=="icon-wifi")
		{
			borrarServicios();
			$("article#enlaces").show();
		} 
		if (servicio=="icon-html")
		{
			borrarServicios();
			$("article#apps").show();
		} 
		if (servicio=="icon-pc")
		{
			borrarServicios();
			$("article#mtto").show();
		} 
	});
	function borrarServicios(){
		$("article#internet").hide();
		$("article#enlaces").hide();
		$("article#apps").hide();
		$("article#mtto").hide();
	}

});
	

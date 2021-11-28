//var ip="localhost:8001";
var ip="api1.jdiaz.live";
var direccion="/CambiarImagen";


function CambiarImagen(){
	console.log('entrega7')
	message ='?';

	$.ajax({

		url: 'http://'+ip+direccion+message,
		crossDomain: true,		   		   
		success: function(response){
			$.each(response,function(key, registro){		    			    				    			    			    
		    	console.log(registro["imagen"].replace("'",""));
				$("#Perfil").attr("src", "/static/media/"+registro["imagen"].replace("'","").replace("'",""))
				
			}); 
			//
			
		},
		error: function(data) {
			console.log(data);
		}
	});   
};
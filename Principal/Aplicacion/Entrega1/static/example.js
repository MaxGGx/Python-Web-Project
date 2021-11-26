var ip="localhost:8001";
var direccion="/CambiarImagen";


function CambiarImagen(){
	console.log('xd')
	message ='?';

	$.ajax({

		url: 'http://'+ip+direccion+message,
		crossDomain: true,		   		   
		success: function(response){
			console.log("xd")
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
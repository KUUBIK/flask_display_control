$('document').ready(function() {
        $.ajaxSetup({
        url: "http://192.168.8.100:8888/static/data.json",
        cache: false,
        dataType: "json",
                        });

		loadData();

});
var lastData = ''
function loadData() {
  	$.getJSON('http://192.168.8.100:8888/static/data.json', function(data) {
  		var out = '';
  		if(data._id == 1){
	      	out += "<div class='layout-center'>";
	      	out += "<img src="+ data.img +">";
	      	out += "</div>";
	      	lastData = data._id;
  		}else if(data._id == 2){
  			out += "<div class='layout-left'>";
	        out += "<img src="+ data.img + ">";
	        out += "</div>";
	        out += "<div class='layout-right'>";
	        out += "<span></span>";
	        out += "<h1>" + data.title + "</h1>";
	        out += "<p>" + data.text + "</p>";
	        out += "</div>";
	        lastData = data._id;
  		}
  		else if(data._id == 3){
  			out += "<video loop muted autoplay";
  			out += " src=" + data.video + " width='100%' height='100%'>";
            out += "Sorry, your browser doesn't support embedded videos."
            out += "</video>"
            lastData = data._id;
  		}else{
  			loadData();
  		}
    	$('.wrapper-content').html(out);
    	setInterval(function(){
    		$.getJSON('http://192.168.8.100:8888/static/data.json', function(data) {
  				if(data._id !== lastData){

   					loadData();
  				}
  			})
  		}, 500);
    })
}




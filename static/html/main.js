$('document').ready(function() {

  setInterval(function(){
  	loadData();
  }, 1000);
});

function loadData() {
  	$.getJSON('localhost:5000', function(data) {
      	var out = '';
      	out += "<div class='layout-left'>";
        out += "<img src="+ data.img + ">";
        out += "</div>";
        out += "<div class='layout-right'>";
        out += "<span></span>";
        out += "<h1>" + data.title + "</h1>";
        out += "<p>" + data.text + "</p>";
        out += "</div>";

    	$('.wrapper-content').html(out);
    })
}

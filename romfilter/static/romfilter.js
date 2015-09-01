
//https://raw.github.com/awbush/jquery-fastLiveFilter/master/jquery.fastLiveFilter.js
//https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css
 function listdone(){
     $('#search_input').fastLiveFilter('#search_list');
     $( "#search_list li" ).click(function() {
        gameid = $(this).attr('id');
        $( ".info").remove();
        //$( this ).css( "color", "red" ); 
         $.get( "/"+gameid+"/info", function( data ) {
		 $("#"+gameid).append( "<div class=\"info\">"+ data.deployed + "</strong>"+'<button type="button" class="btn btn-default btn-lg">
  <span class="glyphicon glyphicon-star" aria-hidden="true"></span> Star
</button>'+"</div>" );
	
}, "json" );
       
	});
 }

$.get( "/all_games", function( data ) {
	var items = [];
	$.each( data, function( shortname, val ) {
    items.push( "<li class=\"list-group-item\" href=\"#\" id='" + shortname + "'><b>" +shortname + "</b> - " + val["name"] + " (" + val["year"] + ") - by " + val["manufacturer"]+ "</li>" );
  });
    $(items.join( "" )).appendTo( "#search_list" );
    listdone();
}, "json" );


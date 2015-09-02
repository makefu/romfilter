
//https://raw.github.com/awbush/jquery-fastLiveFilter/master/jquery.fastLiveFilter.js
//https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css
function infodone(gameid){
  $( "#search_list .btn-success" ).click(function() {
    //$( this ).css( "color", "red" );     
    $.get( "/"+gameid+"/add", function( data ) {
        $('.active').removeClass('active')
        // win,
        $(".btn-success").parent().append("<div class=\"alert alert-success\" role=\"alert\">You successfully added the game.Now go play.</div>");
          $(".btn-success").removeClass(".btn-success").attr("disabled" , "disabled").addClass("btn-danger");

    }).fail( function (data) {
        $(".btn-success").parent().append("<div class=\"alert alert-failed\" role=\"alert\">Something went wrong when trying to add new ROM</div>");
      // something went wrong
    });
  }); //click-search_list
}
function listdone(){
  $('#search_input').fastLiveFilter('#search_list');

  $( "#search_list li div div" ).click(function() {
    gameid = $(this).attr('id');
    $('.active').removeClass('active')
    $(this).parent().addClass('active')
    $( ".info").remove();
    //$( this ).css( "color", "red" );     
    $.get( "/"+gameid+"/info", function( data ) {
      if (data.deployed)
        $("#"+gameid).parent().append( "<div class=\"info\"></strong><button type=\"button\" class=\"btn btn-default btn-danger\" disabled=\"disabled\"><span class=\"glyphicon glyphicon-star\" aria-hidden=\"true\"></span> already deployed</button></div>" );

      else
        $("#"+gameid).parent().append( "<div class=\"info\"></strong><button type=\"button\" class=\"btn btn-default btn-success\"><span class=\"glyphicon glyphicon-star\" aria-hidden=\"true\"></span> deploy</button></div>" );
      
      infodone(gameid)
    }, "json" );
  }); //click-search_list
} // listdone
 
$.get( "/all_games", function( data ) {
  var items = [];
  $.each( data, function( shortname, val ) {
    items.push( "<li ><div class=\"list-group-item\"><div  href=\"#\" id='" + shortname + "'><b>" +shortname + "</b> - " + val["name"] + " (" + val["year"] + ") - by " + val["manufacturer"]+ "</div></div></li>" );
  });
  $(items.join( "" )).appendTo( "#search_list" );
  listdone();
}, "json" );


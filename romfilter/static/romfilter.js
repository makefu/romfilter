
//https://raw.github.com/awbush/jquery-fastLiveFilter/master/jquery.fastLiveFilter.js
//https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css
function activate_button(gameid){
  $( "#deploy_button.btn-enabled" ).click(function() {
    //$( this ).css( "color", "red" );     
    $.get( "/"+gameid+"/add", function( data ) {
        // win,
        $("#"+gameid + " .info").append("<div class=\"alert alert-success\" role=\"alert\">You successfully added the game.Now go play.</div>");
          $(".btn-success").removeClass(".btn-success").attr("disabled" , "disabled").addClass("btn-danger");

    }).fail( function (data) {
        $("#"+gameid+ " .info").append("<div class=\"alert alert-failed\" role=\"alert\">Something went wrong when trying to add new ROM</div>");
      // something went wrong
    });
  }); //click-search_list
}
function listdone(){
  $('#search_input').fastLiveFilter('#search_list');

  $( "#search_list .title" ).click(function() {
    gameid = $(this).parent().attr('id');
    //$('.active').removeClass('active')
    //$(this).parent().addClass('active')
    $( ".info").empty();
    //$( this ).css( "color", "red" );     
    $.get( "/"+gameid+"/info", function( data ) {
        $("#"+gameid +" .info").append(data)
        activate_button(gameid)
    } );
  }); //click-search_list
} // listdone
 
$.get( "/all_games", function( data ) {
  var items = [];
  $.each( data, function( shortname, val ) {
    items.push( "<li ><div class=\"list-group-item\" id=\""+shortname+"\"><div  href=\"#\" class=\"title\" ><b>" +shortname + "</b> - " + val["name"] + " (" + val["year"] + ") - by " + val["manufacturer"]+ "</div><div class=\"info\"></div></div></li>" );
  });
  $(items.join( "" )).appendTo( "#search_list" );
  listdone();
}, "json" );


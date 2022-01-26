$(document).ready( function(){
  // redirect the approval to appropriate view using ajax
  $('.approve').click(function(){
    var journey_id = $(this).attr('id');
    $.ajax({
      type: "POST",
      url : "approve/",
      data:{
        'id': journey_id,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
      },
      datatype: 'json',
      success: function(data){
        if (data['success'])
          location.reload()
      }
    });
  });

});

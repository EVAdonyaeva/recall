$('#signin').submit(function(e){
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
        type: "POST",
        url: "/signin/",
        data: data,
        dataType: "html",
        cache: false,
        statusCode: {
            200: function() {
                window.location.replace('/comment_form')
            },
            401: function(){
                $('#error-signin').html('Authentication error');
            },
            405: function(){
                $('#error-signin').html('Method not allowed');
            }
        }
    });
});

$('#signup').submit(function(e){
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
        type: "POST",
        url: "/signup/",
        data: data,
        dataType: "html",
        cache: false,
        statusCode: {
            200: function() {
                window.location.replace('/comment_form')
            },
            401: function(){
                $('#error-signup').html('Registration error. Probably user with such credentials already exist.');
            },
            405: function(){
                $('#error-signup').html('Method not allowed');
            }
        }
    });
});

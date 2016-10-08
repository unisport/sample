
var update = function(){
    var id = document.getElementById("id").value;
    var url = '/update-product/' + id + '/';
    var data = {
        "id": $("#id").val(),
        "name": $("#name").val(),
        "package": $("#package").is(':checked'),
        "women": $("#women").is(':checked'),
        "price": $("#price").val(),
        "img_url": $("#img_url").val(),
        "price_old": $("#price_old").val(),
        "online": $("#online").is(':checked'),
        "url": $("#url").val(),
        "delivery": $("#delivery").val(),
        "currency": $("#currency").val(),
        "kids": $("#kids").is(':checked'),
        "sizes": $("#sizes").val(),
        "kid_adult": $("#kid_adult").is(':checked'),
        "free_porto": $("#free_porto").is(':checked'),
        "image": $("#image").val()
    };
    $.ajax({
        url: url,
        type: 'PUT',
        data: data,
        success: function(response) {
            bootbox.alert({size: "small", message: "Success! A new product has been updated."});
        },
        error: function(response) {
            bootbox.alert({size: "small", message: "Oops! Something went wrong."});
        }
    });
};

var delete_item = function(){
    var id = document.getElementById("id").value;
    var url = "/product/" + id + "/";
    $.ajax({
        url: url,
        type: 'DELETE',
        success: function(response) {
            bootbox.alert({size: "small", message: "Success! A new product has been deleted."});
        },
        error: function(response) {
            bootbox.alert({size: "small", message: "Oops! Something went wrong."});
        }
    });
};

var save = function(){
    var url = '/product/';
    var data = {
        "name": $("#name").val(),
        "package": $("#package").is(':checked'),
        "women": $("#women").is(':checked'),
        "price": $("#price").val(),
        "img_url": $("#img_url").val(),
        "price_old": $("#price_old").val(),
        "online": $("#online").is(':checked'),
        "url": $("#url").val(),
        "delivery": $("#delivery").val(),
        "currency": $("#currency").val(),
        "kids": $("#kids").is(':checked'),
        "sizes": $("#sizes").val(),
        "kid_adult": $("#kid_adult").is(':checked'),
        "free_porto": $("#free_porto").is(':checked'),
        "image": $("#image").val()
    };
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: function(response) {
            bootbox.alert({size: "small", message: "Success! A new product has been created."});
        },
        error: function(response) {
            bootbox.alert({size: "small", message: "Oops! Something went wrong."});
        }
    });
};
$(document).ready(function () {
    $('#loadButton').click(function (e) {
        e.preventDefault();
        $('#loadButton').prop('disabled', true);
        if (loadDataUrl) {
            $.get(loadDataUrl).done(function (data) {
                if(data && data['success']){
                    $('#statusMessage').text("Data loaded successfully");
                } else {
                    $('#statusMessage').text("Error. Data is not loaded");
                }
                $('#loadButton').prop('disabled', false);
            });
        }

    })
});
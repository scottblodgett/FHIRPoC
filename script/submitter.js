$(document).ready(function () {
    $("#submitButton").click(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        var post_url = "https://2qjivpz9ih.execute-api.us-east-2.amazonaws.com/prod";
        var formValues = $('form').serializeArray()
        form_data = JSON.stringify(formValues);
        //console.log(form_data);
        $.ajax({
            url: post_url,
            type: "POST",
            data: form_data,
            dataType: 'json',
            contentType: 'application/json',
            success: function (data,text) {
                $('#serverResults').html('Basic data for patient ' + data['patientGuid'] + ' received.');
                //console.log(data)
            },
            error: function (xhr, status, errorThrown) {
                console.log(xhr.status + ':' + xhr.responseText)
                $('#serverResults').html('Unexpected error.');
            }
        });
    });
});
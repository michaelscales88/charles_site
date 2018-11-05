function loadAboutPage(api) {
    $.ajax({
        url: api,
        dataType: "JSON",
        success: function (json, statusCode) {
            if (statusCode === 'success') {
                $("#aboutArea").html("About Area");
            }

        }
    })
}
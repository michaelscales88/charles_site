function loadAboutPage(api) {
    $.ajax({
        url: api,
        dataType: "JSON",
        success: function (json, statusCode) {
            if (statusCode === 'success') {
                let aboutArea = "";
                const aboutInfo = JSON.parse(json);
                for (const entry in aboutInfo) {
                    if (aboutInfo.hasOwnProperty(entry)) {
                        aboutArea += `
                            <hr class="col-xs-12 custom-divider">
                            <div class="row">
                                <div class="col-md-4">
                                    <img class="banner-image" src="/static/img/${aboutInfo[entry].path}">
                                </div>
                                <div class="col-md-8">
                                    <h3>${aboutInfo[entry].title}</h3>
                                    <p>${aboutInfo[entry].description}</p>
                                </div>
                            </div>`;
                    }
                }
                $("#aboutArea").html(`
                    <h2>About Us</h2>
                    <div class="container-fluid">
                        ${aboutArea}
                    </div>`
                );
            }

        }
    })
}
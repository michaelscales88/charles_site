function buyNow(id) {
    $.ajax({
        url: "/api/inventory/buy_info",
        method: "POST",
        dataType: "JSON",
        data: JSON.stringify({
            id: id
        }),
        success: function (json, statusCode) {
            if (statusCode === 'success') {
                let buy_info = JSON.parse(json);
                console.log(buy_info);
                $('#buyNowTitle').html(buy_info.name);
                $('#buyNowArea').html(
                    `<div class="container-fluid">
                        <div class="row-fluid text-center">
                            <div class="col-lg-4"><img class="text-center" src='/static/img/${buy_info.path}'></div>
                            <div class="col-lg-4"><b class="text-center">${buy_info.description}</b></div>
                            <div class="col-lg-4">
                                <h3 class="text-center">$ ${buy_info.retail} USD</h3>
                                <div class="text-center">${buy_info.buy_button}</div>
                            </div>
                        </div>
                    </div>`
                );
                $("#buyNowModal").modal("show");
            }
        }
    });
}
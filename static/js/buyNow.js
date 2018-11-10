function buyNow(id) {
    $.ajax({
        url: "/api/inventory/buy_info",
        method: "POST",
        dataType: "JSON",
        data: JSON.stringify({id: id}),
        success: function (json, statusCode) {
            if (statusCode === 'success') {
                const buy_info = JSON.parse(json);
                $('#buyNowTitle').html(buy_info.name);
                $('#buyNowArea').html(
                    `<div class="container-fluid">
                        <div class="row-fluid text-center">
                            <div class="col-lg-4"><img class="text-center" src='/static/img/${buy_info.path}'></div>
                            <div class="col-lg-4"><b class="text-center">${buy_info.description}</b></div>
                            <div class="col-lg-4"><i class="fa fa-dollar"></i><b>${buy_info.retail}</b></div>
                        </div>
                        <div class="row text-center">
                            <div class="text-center">${buy_info.buttons}</div>
                        </div>
                    </div>`
                );
                $("#buyNowModal").modal("show");
            }
        }
    });
}
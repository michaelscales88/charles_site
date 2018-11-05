function getTableDiv(api) {
    return $.ajax({
        url: api,
        dataType: "JSON",
        success: function (json) {
            let $tableDiv = $("#tableDiv");
            let $table = '<table id="displayTable" class="table table-striped table-bordered" ' +
                '       cellspacing="0" width="100%" data-placement="top" ' +
                '       title="Scroll left or right to see more information."><thead><tr>' +
                '       </tr></thead></table>';

            $tableDiv.empty();
            $tableDiv.append($table);

            $.each(json.columns, function (i, val) {
                $('#displayTable thead tr').append("<th>" + val[0].toUpperCase() + val.slice(1) + "</th>")
            });
            $('#displayTable thead tr').append("<th>Buy Now</th>");

            let data = [];
            $.each(JSON.parse(json.data), function (i, val) {
                data.push([]);
                $.each(json.columns, function (j, col) {
                    if (col === 'retail') data[i].push(`<i class="fa fa-dollar"></i><b>${val[col]}</b>`);
                    else data[i].push(`<b>${val[col]}</b>`);
                });
                let button = '<button class="btn btn-primary text-center" style="width: 100%;" onclick="buyNow(' + val.id + ')">' +
                    '<i class="fa fa-shopping-cart" style="font-size:24px"></i></i></button>';
                data[i].push(button);
            });

            $('table.table').DataTable({
                responsive: true,
                processing: true,
                paging: false,
                pageLength: -1,
                scrollX: true,
                scrollY: 400,
                scrollCollapse: true,
                data: data
            });
        }
    });
}
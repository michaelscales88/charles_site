let $btn = $('a#topButton');
let $winCached = $(window),
    $docCached = $(document);

$winCached.scroll(function () {
    if (
        $winCached.scrollTop() + $winCached.height()
        > $docCached.height() - 200
    ) $btn.show();
    else $btn.hide();
});

$btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({scrollTop: 0}, '300');
});

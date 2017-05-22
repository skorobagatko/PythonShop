$(function () {

    showbasket();

    $(".buy").click(function () {
        var arr = $.cookie('cart');
        if (!arr) {
            arr = '[]';
        }
        var json = $.parseJSON(arr);
        json.push({
            'name': $('h1').text(),
            'price': $('span.value').text(),
            'img': $('img.full').attr('src')
        });
        $.cookie('cart', JSON.stringify(json), {path: '/'});

        var summa = 0;
        $.each(json, function (index, value) {
            summa += parseInt(value['price']);
        });
        $('.cart .summa').text(summa);
    });
});

function showbasket() {
    var arr = $.cookie('cart');
    if (!arr) {
        arr = '[]';
    }
    var json = $.parseJSON(arr);
    var summa = 0;
    $.each(json, function (index, value) {
        summa += parseInt(value['price']);
    });
    $('.cart .summa').text(summa);
}
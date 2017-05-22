$(function () {
    var arr = $.cookie('cart');
    if (!arr) {
        arr = '[]';
    }
    var json = $.parseJSON(arr);
    var summa = 0;
    $.each(json, function (index, value) {
        $('.order').append('<div class="row"><div class="id" style="display:none">' + index + '</div>' +
            '<img src="' + value["img"] + '"><div class="name">' + value["name"] +
            '</div><div class="price">' + value["price"] + '</div><div class="remove">X</div></div>');
        summa += parseInt(value['price']);
    });
    $('.total .summa').text(summa);

    $('.remove').on('click', function () {
        var parent = $(this).parent();
        var id = parseInt($(this).closest('.row').find('.id').text());

        var arr1 = $.cookie('cart');
        if (!arr1) {arr = '[]';}
        var json1 = $.parseJSON(arr1);
        var summa1 = parseInt($('.total .summa').text());
        $.each(json, function (index, value) {
            if (index==id) {
                summa1 = summa1 - parseInt(value['price']);
                json1.splice(index, 1);
            }
        });
        $.cookie('cart', JSON.stringify(json1), {path: '/'});
        $('.total .summa').text(summa1);
        parent.remove();

        $.each('.id', function (index, value) {
            $(this).text(index);
        });
    });
});
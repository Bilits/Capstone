
//  Preloader
jQuery(window).on("load", function () {
    $('#preloader').fadeOut(500);
    $('#main-wrapper').addClass('show');
});


(function ($) {

    // Selectbox
    $('select').niceSelect();


    // Menu Activation
    $(function () {
        for (var nk = window.location,
            o = $(".menu a, .sub-menu a").filter(function () {
                return this.href == nk;
            })
                .addClass("active")
                .parent()
                .addClass("active"); ;) {
            // console.log(o)
            if (!o.is("li")) break;
            o = o.parent()
                .addClass("show")
                .parent()
                .addClass("active");
        }

    });


    // Tool Tip
    $('[data-toggle="tooltip"]').tooltip();

    // Table row click icon
    $('.data-close').on('click', function () {
        e.preventDefault();
        $(this).parent().parent().remove();
    });

    // Table row delete
    $("#tbUser").on('click', '.btnDelete', function () {
        $(this).closest('tr').remove();
    });


    // Leverage pricing slider
    $(function () {
        var slider = document.getElementById("slider");
        slider.oninput = function () {
            $('.count').text(this.value).css({
                'left': this.value + '%',
                'transform': 'translateX(-' + this.value + '%)'
            });
            $('.fill').css('width', this.value + '%');
        }
    });


})(jQuery);;







const ml = new PerfectScrollbar('.market-limit');
const mn = new PerfectScrollbar('.market-nested');
const ln = new PerfectScrollbar('.limit-nested');
const sln = new PerfectScrollbar('.stop-limit-nested');
const pp = new PerfectScrollbar('.price-pair');
const ts = new PerfectScrollbar('.trade-history');
const ob = new PerfectScrollbar('.order-book');
const yp = new PerfectScrollbar('.your-position');
const bw = new PerfectScrollbar('.balance-widget');
const mkn = new PerfectScrollbar('.market-news');
const opt = new PerfectScrollbar('.open-position-table');

//ripple effect on button
Waves.init();
Waves.attach('.wave-effect');
Waves.attach('.btn');
Waves.attach('button');
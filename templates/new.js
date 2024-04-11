$(document).ready(function() {
    $(window).scroll(function() {
        var windowHeight = $(window).height();
        var scrollTop = $(window).scrollTop();
        var sectionOffset = $('#hero').offset().top;

        if (scrollTop > (sectionOffset - windowHeight + 200)) {
            $('#capture, #captioncapture').addClass('loaded');
        }
    });
});

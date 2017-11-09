$('.rbac-menu-header').click(function () {
    var $icon = $(this).children().first();
    if($icon.hasClass('glyphicon-folder-open')){
        $icon.removeClass('glyphicon-folder-open').addClass('glyphicon-folder-close');
    }else{
        $icon.removeClass('glyphicon-folder-close').addClass('glyphicon-folder-open');
    }
    $(this).next().toggleClass('rbac-hide');
});
  function hi(){
    $('.drop').droppable({
    tolerance: 'intersect',
    drop: function(event, ui) {
        var drop_p = $(this).offset();
        var drag_p = ui.draggable.offset();
        var left_end = drop_p.left - drag_p.left + 1;
        var top_end = drop_p.top - drag_p.top + 1;
        ui.draggable.animate({
            top: '+=' + top_end,
            left: '+=' + left_end
        });
    }
});

$('.boxArt').draggable({
    revert: 'invalid',
    scroll: false,
    stack: ".boxArt"
});
}
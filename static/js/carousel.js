// Generated by CoffeeScript 1.3.1
(function() {
  var carousel, next, prev, slide;

  slide = function(pixels) {
    var curr, inner, left;
    inner = $('.carousel-inner')[0];
    curr = inner.style.left;
    curr = parseInt(curr.replace(/px/, ''));
    left = (curr + pixels).toString() + 'px';
    return $(inner).animate({
      'left': left
    }, 200);
  };

  prev = function() {
    slide(650);
    $('.carousel-inner .active').prev().addClass('prev');
    $('.carousel-inner .active').removeClass('active');
    $('.carousel-inner .prev').addClass('active');
    $('.carousel-inner .active').removeClass('prev');
    return carousel();
  };

  next = function() {
    slide(-650);
    $('.carousel-inner .active').next().addClass('next');
    $('.carousel-inner .active').removeClass('active');
    $('.carousel-inner .next').addClass('active');
    $('.carousel-inner .active').removeClass('next');
    return carousel();
  };

  carousel = function() {
    $('.carousel-inner .active').unbind();
    $('.carousel-inner .active').next().unbind();
    $('.carousel-inner .active').prev().unbind();
    $('.carousel-inner .active').next().click(next);
    return $('.carousel-inner .active').prev().click(prev);
  };

  $(document).ready(function() {
    return carousel();
  });

}).call(this);
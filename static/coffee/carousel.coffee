slide = (pixels) ->
	inner = $('.carousel-inner')[0]
	curr = inner.style.left
	curr = parseInt(curr.replace /px/, '')
	left = (curr + pixels).toString() + 'px'
	$(inner).animate({'left': left}, 200)


prev = ->
	$('.carousel-inner .active').fadeTo(200, .5)
	$('.carousel-inner .active').prev().fadeTo(200, 1)
	$('.carousel-inner .active').prev().addClass('prev')
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .prev').addClass('active')
	$('.carousel-inner .active').removeClass('prev')
	carousel()
	slide(650)


next = ->
	$('.carousel-inner .active').fadeTo(200, .5)
	$('.carousel-inner .active').next().fadeTo(200, 1)
	$('.carousel-inner .active').next().addClass('next')
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .next').addClass('active')
	$('.carousel-inner .active').removeClass('next')
	carousel()
	slide(-650)


carousel = ->
	$('.carousel-inner .active').unbind()
	$('.carousel-inner .active').next().unbind()
	$('.carousel-inner .active').prev().unbind()
	$('.carousel-inner .active').next().click(next)
	$('.carousel-inner .active').prev().click(prev)


$(document).ready ->
	carousel()
	$('.landing a.arrow').click(->
		$('.landing').hide()
		$('.carousel').show()
	)
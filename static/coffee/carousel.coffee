slide = (pixels) ->
	inner = $('.carousel-inner')[0]
	curr = inner.style.left
	curr = parseInt(curr.replace /px/, '')
	left = (curr + pixels).toString() + 'px'
	$(inner).animate({'left': left}, 200)


prev = ->
	slide(650)
	$('.carousel-inner .active').prev().addClass('prev')
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .prev').addClass('active')
	$('.carousel-inner .active').removeClass('prev')
	carousel()


next = ->
	slide(-650)
	$('.carousel-inner .active').next().addClass('next')
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .next').addClass('active')
	$('.carousel-inner .active').removeClass('next')
	carousel()


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
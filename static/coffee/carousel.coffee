interval = 200
opacity = .5
sliding = false


slide = (pixels) ->
	inner = $('.carousel-inner')[0]
	curr = inner.style.left
	curr = parseInt(curr.replace /px/, '')
	left = (curr + pixels).toString() + 'px'
	sliding = true
	$(inner).animate({'left': left}, interval, -> sliding = false)


moveTo = (sibling) ->
	return unless $('.carousel-inner .active')[sibling]().length
	return if sliding
	$('.carousel-inner .active').fadeTo(interval, opacity,
		-> $(this).css({'opacity': ''})
	)
	$('.carousel-inner .active')[sibling]().fadeTo(interval, 1,
		-> $(this).css({'opacity': ''})
	)
	$('.carousel-inner .active')[sibling]().addClass(sibling)
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .' + sibling).addClass('active')
	$('.carousel-inner .active').removeClass(sibling)
	resetCarousel()
	pixels = if sibling == 'prev' then 650 else -650
	slide(pixels)


prev = ->
	moveTo('prev')


next = ->
	moveTo('next')


resetCarousel = ->
	$('.carousel-inner .active').unbind()
	$('.carousel-inner .active').next().unbind()
	$('.carousel-inner .active').prev().unbind()
	$('.carousel-inner .active').next().click(next)
	$('.carousel-inner .active').prev().click(prev)


startCarousel = ->
	$('.landing').hide()
	$('.carousel').show()
	resetCarousel()
	$(document).keydown (e) ->
		if e.keyCode == 37  # left
			moveTo('prev')
			return false
		else if e.keyCode == 39  # right
			moveTo('next')
			return false


$(document).ready ->
	$('.landing .arrow').click(->
		startCarousel()
	)
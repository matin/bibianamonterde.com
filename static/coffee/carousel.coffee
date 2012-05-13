interval = 200
lastSlide = 0


slide = (pixels) ->
	inner = $('.carousel-inner')[0]
	curr = inner.style.left
	curr = parseInt(curr.replace /px/, '')
	left = (curr + pixels).toString() + 'px'
	$(inner).animate({'left': left}, interval)


doubleKeypress = ->
	now = new Date()
	if now - lastSlide <= interval
		return true
	else
		lastSlide = now
		return false


moveTo = (sibling) ->
	return unless $('.carousel-inner .active')[sibling]().length
	return if doubleKeypress()
	$('.carousel-inner .active').fadeTo(interval, .5)
	$('.carousel-inner .active')[sibling]().fadeTo(interval, 1)
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
	$('.landing a.arrow').click(->
		startCarousel()
	)
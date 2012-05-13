slide = (pixels) ->
	inner = $('.carousel-inner')[0]
	curr = inner.style.left
	curr = parseInt(curr.replace /px/, '')
	left = (curr + pixels).toString() + 'px'
	$(inner).animate({'left': left}, 200)

moveTo = (sibling) ->
	$('.carousel-inner .active').fadeTo(200, .5)
	$('.carousel-inner .active')[sibling]().fadeTo(200, 1)
	$('.carousel-inner .active')[sibling]().addClass(sibling)
	$('.carousel-inner .active').removeClass('active')
	$('.carousel-inner .' + sibling).addClass('active')
	$('.carousel-inner .active').removeClass(sibling)
	carousel()
	slide(650 if sibling == 'prev' else -650)

prev = ->
	moveTo('prev')


next = ->
	moveTo('next')


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
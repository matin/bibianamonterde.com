$(document).ready(function() {
	$('#carousel-inner').carouFredSel({
		width: '100%',
		items: 3,
		scroll: {
			items: 1,
			duration: 1000,
			pauseDuration: 3000
		},
		auto: {
			play: false
		},
		prev: '#prev',
		next: '#next'
	});
});
BOOTSTRAP = ../css/bootstrap.css
BOOTSTRAP_LESS = ./boostrap.less


build:
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}


watch:
	echo "Watching less files... "; \
	watchr -e "watch('.*\.less') { system 'make' }"
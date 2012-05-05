BOOTSTRAP = ../css/bootstrap.css
BOOTSTRAP_LESS = ./bootstrap/bootstrap.less


build:
	@echo "Building Bootstrap..."
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}


watch:
	@echo "Watching less files..."
	@watchr -e "watch('.*\.less') { system 'make' }"
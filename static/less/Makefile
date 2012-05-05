CSS = ../css
BOOTSTRAP = ${CSS}/bootstrap.css
BOOTSTRAP_LESS = ./bootstrap/bootstrap.less


build:
	@echo "Building Bootstrap..."
	@mkdir -p ${CSS}
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	@recess --compile bibiana.less > ../css/bibiana.css
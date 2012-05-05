import os

from flask import abort, Flask, render_template
from jinja2 import Markup


app = Flask(__name__)


@app.template_filter('preview')
def preview_filter(args):
    snippet = """
    <div class="span12 preview" style="background-image:url('{image}');">
		<span class="orange">
            <span class="number">
    			<span class="section">{section[0]}</span>
                <span class="slash">/</span>
    			<span class="project">{project[0]}</span>
  		    </span>
            <span class="text">
    			<span class="section">{section[1]}</span>
    			<span class="project">/ {project[1]}</span>
            </span>
        </span>
    </div>"""
    return Markup(snippet.format(**args))


@app.template_filter('menu_section')
def menu_section_filter(args):
    snippet = """
    <li class="section">
		<a href="/{name_lower}">
			<span class="number">{number}</span>
			<span class="slash">/</span>
			<span class="name">{name}</span>
		</a>
	</li>"""
    return Markup(snippet.format(name_lower=args['name'].lower(), **args))


@app.route('/')
def home():
    files = os.listdir('static/img/home')
    images = ['/static/img/home/' + file for file in files if file.endswith('.png')]
    return render_template('home.html', images=images)


@app.route('/<section_name>')
def section(section_name):
    img_location = 'static/img/{}'.format(section_name)
    if not os.path.exists(img_location):
        abort(404)
    files = os.listdir(img_location)
    images = ['/{}/{}'.format(img_location, file) for file in files if file.endswith('.png')]
    template = render_template('section.html', images=images)
    return template


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from collections import defaultdict
import os

from flask import abort, Flask, request, render_template
from jinja2 import Markup


app = Flask(__name__)


img_folder = os.path.join(app.static_folder, 'img')
tree = defaultdict(list)

for section in os.listdir(img_folder):
    section_folder = os.path.join(img_folder, section)
    if not (section[:2].isdigit() and os.path.isdir(section_folder)):
        continue
    section = (section[:2], section[2:].replace('-', ' '))

    for project in os.listdir(section_folder):
        project_folder = os.path.join(section_folder, project)
        if not (project[:2].isdigit() and os.path.isdir(project_folder)):
            continue
        project = (project[:2], project[2:].replace('-', ' '))
        tree[section].append(project)


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
    section_class = ''
    if request.url.endswith('{number}{name}'.format(**args)):
        section_class = 'selected'
    snippet = """
    <li class="section">
		<a href="/{number}{name}" class="{section_class}">
			<span class="number">{number}</span>
			<span class="slash">/</span>
			<span class="name">{name_upper}</span>
		</a>
	</li>""".format(
        name_upper=args['name'].upper(),
        section_class=section_class,
        **args
    )
    return Markup(snippet)


@app.route('/')
@app.route('/<section>')
def preview(section='home'):
    location = 'static/img/{}'.format(section)
    if not os.path.isdir(location):
        abort(404)
    files = os.listdir(location)
    images = ['/{}/{}'.format(location, image) for image in files if image.endswith('.png')]

    return render_template('grid.html', tree=tree, images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

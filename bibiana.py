from collections import defaultdict
import re
import os

from flask import abort, Flask, request, render_template
from jinja2 import Markup


app = Flask(__name__)


img_folder = os.path.join(app.static_folder, 'img')
tree = defaultdict(list)

def build_tree():
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
    return tree


def get_projects(section):
    section_folder = os.path.join(app.static_folder, 'img', section)
    projects = defaultdict(dict)

    images = os.listdir(section_folder)
    project_re = re.compile("""
        \d\.  # leading digit for sorting
        (?P<section_number>\d{2})(?P<section_name>[^.]+)\.  # section
        (?P<project_number>\d{2})(?P<project_name>[^.]+)\.  # project
        (?:png|jpg)$""", re.VERBOSE)

    for image in images:
        if not (image.endswith('.png') or image.endswith('.jpg')):
            continue
        m = project_re.match(image)
        if m:
            projects[image] = m.groupdict()
            projects[image]['url'] = ('/{section_number}{section_name}/'
                '{project_number}{project_name}'.format(**m.groupdict()))
        projects[image]['image_url'] = '{}/img/{}/{}'.format(
            app.static_url_path, section, image)
    return projects


TREE = build_tree()


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


@app.route('/')
@app.route('/<section>')
def grid(section='home'):
    location = 'static/img/{}'.format(section)
    if not os.path.isdir(location):
        abort(404)
    files = os.listdir(location)
    images = ['/{}/{}'.format(location, image) for image in files if image.endswith('.png')]

    return render_template('grid.html', tree=TREE, projects=get_projects(section), images=images, section=section)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

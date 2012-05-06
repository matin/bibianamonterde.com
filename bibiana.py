from collections import defaultdict
import re
import os

from flask import abort, Flask, render_template


app = Flask(__name__)


def build_tree():
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
    return tree


def get_projects(section):
    section_folder = os.path.join(app.static_folder, 'img', section)
    projects = defaultdict(dict)

    images = os.listdir(section_folder)
    project_re = re.compile("""
        [^.]+\.  # set for order
        (?P<section_number>\d{2})(?P<section_name>[^.]+)\.  # section
        (?P<project_number>\d{2})(?P<project_name>[^.]+)\.  # project
        (?:png|jpg)$""", re.VERBOSE)

    for image in images:
        if not (image.endswith('.png') or image.endswith('.jpg')):
            continue
        m = project_re.match(image)
        if m:
            projects[image] = m.groupdict()
            projects[image]['section_name'] = projects[image]['section_name'].replace('-',' ')
            projects[image]['project_name'] = projects[image]['project_name'].replace('-',' ')
            projects[image]['url'] = ('/{section_number}{section_name}/'
                '{project_number}{project_name}'.format(**m.groupdict()))
        projects[image]['image_url'] = '{}/img/{}/{}'.format(
            app.static_url_path, section, image)
    return projects


TREE = build_tree()


@app.route('/')
@app.route('/<section>')
def grid(section='home'):
    if not os.path.isdir('static/img/{}'.format(section)):
        abort(404)
    return render_template('grid.html', tree=TREE, section=section,
        projects=get_projects(section))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from collections import defaultdict
import re
import os

from flask import (abort, Flask, redirect, render_template, request, session,
    url_for)


app = Flask(__name__)
app.secret_key = 'e+moUemdz7GkrjiIb+xIp8M1szMrx7KNvBAO'


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
            projects[image]['section_name'] = (projects[image]['section_name']
                .replace('-',' '))
            projects[image]['project_name'] = (projects[image]['project_name']
                .replace('-',' '))
            projects[image]['url'] = ('/{section_number}{section_name}/'
                '{project_number}{project_name}'.format(**m.groupdict()))
        projects[image]['image_url'] = '{}/img/{}/{}'.format(
            app.static_url_path, section, image)
    return projects


def logged_in():
    return 'authed' in session


def requires_auth(controller):
    def decorator(*args, **kwargs):
        if not logged_in():
            return redirect(url_for('index'))
        else:
            return controller(*args, **kwargs)


TREE = build_tree()


@app.route('/login')
def login():
    session['authed'] = 'true'
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if logged_in():
        session.pop('authed')
    return redirect(url_for('index'))


@app.route('/')
def index():
    if logged_in():
        resp = render_template('grid.html', tree=TREE, section='home',
            projects=get_projects('home'))
    else:
        resp = render_template('login.html', section='password',
            projects=get_projects('password'))
    return resp


@requires_auth
@app.route('/<section>')
def grid(section):
    if not os.path.isdir('static/img/{}'.format(section)):
        abort(404)
    return render_template('grid.html', tree=TREE, section=section,
        projects=get_projects(section))


if __name__ == '__main__':
    app.debug = os.environ.get('BIBIANA') == 'debug' or False
    app.run(host='0.0.0.0')

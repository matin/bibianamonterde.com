import os

from flask import Flask, render_template
from jinja2 import Markup


app = Flask(__name__)


@app.template_filter('preview')
def preview(kwargs):
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
    return Markup(snippet.format(**kwargs))


@app.route('/')
def home():
    files = os.listdir('static/img/home')
    images = ['/static/img/home/' + file for file in files if file.endswith('.png')]
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

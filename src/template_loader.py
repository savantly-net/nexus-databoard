from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from config import project_dir

env = Environment(
    loader=FileSystemLoader(f"{project_dir}/src/templates"),
    autoescape=select_autoescape()
)

def render_template(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)
import yaml
import jinja2

"""
Jinja2 is a templating engine that is very commonly used for templating out network device configurations,
but is capable of much more.
"""

def generate_config():
    """
    Generate BGP config from template
    """
    config_data = yaml.safe_load(open("yaml_bgp.yaml"))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("bgp_template.j2")
    configuration = template.render(config_data)
    print(configuration)
    

if __name__ == "__main__":
    generate_config()
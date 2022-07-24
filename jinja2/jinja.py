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

    # The Environment object is the central object used in the Jinja2 module.
    # The loader argument can be used to load templates
    env = jinja2.Environment(
        # FileSystemLoader can be used to load tempalres from a directory in the file system ./templates in this case.
        loader=jinja2.FileSystemLoader("./templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("bgp_template.j2")
    # template = env.get_template("snmp.j2")
    configuration = template.render(config_data)
    print(configuration)


if __name__ == "__main__":
    generate_config()

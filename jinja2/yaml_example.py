import yaml
import json


def main():

    parsed_yaml_data = yaml.safe_load(open("yaml_bgp.yaml"))
    print(json.dumps(parsed_yaml_data, indent=4))
    print(type(parsed_yaml_data))


if __name__ == "__main__":
    main()

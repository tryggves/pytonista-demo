# Do some testing of YAML document structures and how they appear in Python code.

from typing import Dict
import yaml


def _get_yaml_file_content(file_name: str) -> Dict:
    with open(file_name, "r") as in_file:
        try:
            return yaml.safe_load(in_file)
        except yaml.YAMLError as exc:
            print(f'Could not load file {exc}')


yaml_dict = _get_yaml_file_content("demo1.yaml")
print(f"Yaml document is: {yaml_dict}")
yaml_dict = _get_yaml_file_content("demo2.yaml")
print(f"Yaml document is: {yaml_dict}")
yaml_dict = _get_yaml_file_content("demo3.yaml")
print(f"Yaml document is: {yaml_dict}")
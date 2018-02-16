import yaml


def parse_yml(config='loader.yml'):
    """
    Creates a dictionary from config file
    :type config: string
    :rtype: dict
    """
    with open(config) as yml_file:
        dictionary = yaml.load(yml_file)
        return dictionary

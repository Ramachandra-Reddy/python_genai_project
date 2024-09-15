import yaml

def load_config(env_name):
    with open(config.yaml, "r") as config_file:
        config_data = yaml.safe_load(config_file)
        return config_data[env_name]

CONFIG = load_config("dev")
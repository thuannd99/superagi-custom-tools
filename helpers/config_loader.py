import yaml

class ConfigLoader:
    def __init__(self, filename="config.yaml"):
        self.filename = filename
        self._config = self._load_config()

    def _load_config(self):
        with open(self.filename, 'r') as file:
            try:
                config = yaml.safe_load(file)
                return config
            except yaml.YAMLError as exc:
                print(f"Error loading YAML file: {exc}")
                return None

    def get(self, *args, default=None):
        result = self._config
        for key in args:
            if isinstance(result, dict):
                result = result.get(key)
            else:
                return default
        return result if result is not None else default

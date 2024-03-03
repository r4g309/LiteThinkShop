import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name: str, default: str = None) -> str:
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)

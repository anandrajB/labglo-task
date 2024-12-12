import importlib
import os
import subprocess

from termcolor import colored

from .base import *

__all__ = ["base"]
env = os.getenv("APP_ENV", "LOCAL")


def print_message_and_import_settings(env, module_name):
    print(colored(f"USING {env.upper()} SETTINGS", "green", attrs=["bold"]))

    importlib.import_module(f".{module_name}", package=__package__)
    subprocess.Popen(
        "export DJANGO_SETTINGS_MODULE=tfm.settings", shell=True, stdout=subprocess.PIPE
    ).stdout.read()


env_settings = {
    "PROD": "prod",
    "TEST": "test",
    "LOCAL": "local",
}

if env in env_settings:
    print_message_and_import_settings(env, env_settings[env])
    # if env == "LOCAL":
    #     from .local import *
    # elif env == "TEST":
    #     from .test import *
    # elif env == "PROD":
    #     from .prod import *
else:
    raise Exception(
        colored(
            "APP_ENV must be set to run the project, example: export APP_ENV=LOCAL / TEST / PROD",
            "red",
            attrs=["bold"],
        )
    )

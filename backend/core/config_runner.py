# config/config_runner.py
import os
from backend import server


def get_log_dir(log_name):
    log_dir = os.path.join(server.config["LOGS_DIR"], log_name)
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


os.makedirs("instance/", exist_ok=True)


for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith("_config.py"):
            module, *d = file.split("_")
            try:
                path = os.path.abspath(os.path.join(root, file))
                server.config.from_pyfile(path)
            except FileNotFoundError:
                print("Failed to load [ {module_name} ] module settings.".format(module_name=module))
            else:
                print("Loaded [ {module_name} ] module settings.".format(module_name=module))

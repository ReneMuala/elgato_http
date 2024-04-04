import os

project_name = "Elgato http"

packages = ['requests']

_packages_str = ", ".join(packages)

print(f"PROJECT: {project_name}\n PACKAGES: {_packages_str}")

for package in packages:
    if os.system(f"pip3 install {package}") != 0:
        os.system(f"pip install {package}")
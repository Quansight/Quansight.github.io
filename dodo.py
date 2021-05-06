orgs= "scipy numpy Quansight Quansight-labs pytorch Napari IPython zarr-developers ibis-project"
import doit


def task_convert():
    return dict(
        file_dep=["index.ipynb"],
        actions=[
            "jupyter nbconvert --to html --TemplateExporter.exclude_input=True --TemplateExporter.exclude_output_prompt=True index.ipynb",
            "jupyter nbconvert --to html  --stdout index.ipynb >> developer.html"
        ],
        targets=["index.html", "developer.html"]
    )
    
def get_info(project):
    import requests_cache, requests
    print(F"https://api.github.com/orgs/{project}")
    return requests.get(F"https://api.github.com/orgs/{project}").json()

def create_db(projects):
    import pandas
    import json
    print(projects)
    with open("projects.json", "w") as f:
            f.write(json.dumps(list(map(get_info, projects))))

def task_db():
    return dict(
        actions=[(create_db, (orgs.split(),), {})],
        targets=["projects.json"]
    )
    
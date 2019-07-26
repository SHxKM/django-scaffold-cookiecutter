# project slug validation inspired by https://github.com/pydanny/cookiecutter-django/blob/master/hooks/pre_gen_project.py

project_slug = "{{ cookiecutter.project_slug }}"

if hasattr(project_slug, "isidentifier"):
    assert (
        project_slug.isidentifier()
    ), f"project slug ({project_slug}) is not a valid Python identifier."

assert (
    project_slug == project_slug.lower()
), f"{project_slug} project slug should be all lowercase"

assert (
    "\\" not in "{{ cookiecutter.author_name }}"
), "Don't include backslashes in author name."

# Scaffold Django X: a flexible cookiecutter

A cookiecutter that's simple yet flexible for quick scaffolding of Django projects. Save on boilerplate code and start prototyping/developing within seconds.

### Includes:

- CSS framework (optional): [Bootstrap 4](https://getbootstrap.com/docs/4.3/getting-started/introduction/) | [Tailwind CSS](https://tailwindcss.com/) (default) | none 
- jQuery CDN (default: no)
- A simple `base.html` file: specific structure depends on the CSS framework you choose
- An empty `main.js` in `static/your_project/javascript/` that's included in `base.html`
- An empty `main.css` in `static/your_project/css/` that's included in `base.html`
- A `.gitignore` with sane defaults
- `Pipfile` for `pipenv` support: structure depends on the options you choose
- A simple, `gitignore`d `.env` file for environment variable management (with the pre-installed `python-decouple`)
- A top level `tests` folder
- `.pylintrc` file for basic Python linting (pre-installed: `pylint` and `pylint-django`)
- `.eslintrc` file for basic JavaScript linting.

### Dependencies

Requires: [`cookiecutter`](https://github.com/audreyr/cookiecutter)

### How to use


1. Make sure you have installed [all the dependencies](#dependencies).
2. Navigate to the folder in which you want to scaffold your Django project
3. run `cookiecutter path_or_url/to/this/repository`
4. Fill in your project's details
5. run `pipenv install`
6. run `pipenv shell` to enter your virtual environment
7. `python manage.py migrate` to run the initial migration
8. `python manage.py runserver` to start the dev server at `localhost:8000`
9. Profit

### Contributions

Contributions that keep this project flexible and simple are more than welcome. Feel free to fork this repository and adapt it for any of your needs.

### Changelog & TODO (help welcome)

- [ ] Support for optional DRF/Rest-API scaffolding
- [ ] Support for optional Django Debug Toolbar
- [ ] Support for `django-compressor`
- [ ] Add tests 

### Questions?

Read the tutorial (coming soon) or [get in touch](https://twitter.com/SHxKM).
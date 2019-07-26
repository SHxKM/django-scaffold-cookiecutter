import os
import shutil


def remove_tailwind_folder():
    print("You chose to not use TailWind CSS - removing its directory and config")
    theme_dir_path = "theme"
    if os.path.exists(theme_dir_path):
        shutil.rmtree(theme_dir_path)


def prepend_env_file_to_gitignore():
    envfile_path = ".gitignore"
    if os.path.exists(envfile_path):
        print("prenpending .env file to .gitignore")
        with open(envfile_path, "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write(".env".rstrip("\r\n") + "\n" + content)


def main():
    if "{{cookiecutter.css_framework}}".lower() != "tailwindcss":
        remove_tailwind_folder()

    prepend_env_file_to_gitignore()


if __name__ == "__main__":
    main()

import toml

def generate_code():
    with open('pyproject.toml', 'r') as file:
        pyproject_data = toml.load(file)

    if 'tool' in pyproject_data and 'poetry' in pyproject_data['tool']:
        dependencies = pyproject_data['tool']['poetry'].get('dependencies', {})
        import_code = []
        modules_list = []



        for package, version in dependencies.items():
            if package.startswith("module"):
                import_statement = f"import {package}"
                import_code.append(import_statement)
                modules_list.append(package)


        with open('.\\camera_service\\modules\\modules_list.py', 'w') as out_file:
            out_file.write('\n'.join([*import_code, "\n", "modules = [", ", ".join(modules_list), "]"]))

if __name__ == "__main__":
    generate_code()
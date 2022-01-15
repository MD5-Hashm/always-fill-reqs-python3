import packages as pkg
packages = ["flask", "os"]
exec(pkg.import_packages(packages))
print(os.getcwd())
# WSL Should now work

# always-fill-reqs-python3
Always fill your package requirements without the user having to do anything! Simple and easy!

# Supported platforms

As far as I've tested this works on every system running python3

# Usage
View /tests/expariment1 for an example or follow this:

Include packages.py in your main files directory

Then import packages.py in your main file:

```Import packages as pkg```

At the top of your main file include a packages list with the packages you want like so:

```packages = ["os", "flask", "requests", "random", "json"]```

Then include this one liner to install and import all the required packages:

```exec(pkg.import_packages(packages))```

Your ide will probably complain that the packages arent imported (even though they are) so feel free to import them the normal way while writing your code.

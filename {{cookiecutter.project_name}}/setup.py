#!/usr/bin/env python

###############################################################################
#     {{cookiecutter.project_name}}
#
#     Copyright (C) 2019  MAX IV Laboratory, Lund Sweden.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

from setuptools import setup, find_packages


def main():
    """Main method collecting all the parameters to setup."""
    name = "{{cookiecutter.project_name}}"

    version = "0.0.0"

    description = "{{cookiecutter.project_description}}"

    author = "{{cookiecutter.author_name}}"

    author_email = "{{cookiecutter.author_email}}"

    license = "GPLv3"

    url = "http://www.maxiv.lu.se"

    packages = find_packages()

    # Add your dependencies in the following line.
    install_requires = ['sardana']

    setup(
        name=name,
        version=version,
        description=description,
        author=author,
        author_email=author_email,
        license=license,
        url=url,
        packages=packages,
        install_requires=install_requires
    )

if __name__ == "__main__":
    main()

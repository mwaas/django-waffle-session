======
README
======

Django Waffle is (yet another) feature flipper for Django. You can
define the conditions for which a flag should be active, and use it in
a number of ways.

.. image:: https://travis-ci.org/jsocol/django-waffle.png?branch=master
   :target: https://travis-ci.org/jsocol/django-waffle
   :alt: Travis-CI Build Status

:Code:          https://github.com/jsocol/django-waffle
:License:       BSD; see LICENSE file
:Issues:        https://github.com/jsocol/django-waffle/issues
:Documentation: http://waffle.readthedocs.org/


# Contributing to Waffle
Waffle is pretty simple to hack, and has a decent test suite! Here’s how to hack Waffle, add tests, run them, and contribute changes.

1. Clone this repo

2. Set Up          
Setting up an environment is easy! You’ll want virtualenv and pip, then just create a new virtual environment and install the requirements:

`$ mkvirtualenv waffle`
`$ pip install -r requirements.txt`       
Done!

3. Running Things             
Waffle comes with a helper shell script to run tests and create schema migrations: run.sh. To run the tests, just:

`$ ./run.sh test`      
Run the script with no arguments to see all the options.


Django Waffle releases are based on Semantic Versioning. Please refer to
the [Semantic Versioning documentation](http://semver.org/) for
reference.

- Make code changes on master branch
- Update setup.py with the new version number
- `git commit`
- `git tag -a vMAJOR.MINOR.PATCH -m "my version MAJOR.MINOR.PATCH"`
- `git push`
- `git push --tags`
- `make distribute`
- Upload the new tar django-waffle-session version from the `dist` directory to [Jumo-nexus](https://repository.jumo.world/) under the repository jumo-pypi
- make relevant changes in your code to utilize the updated version.
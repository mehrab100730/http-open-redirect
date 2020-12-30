pretty:
        find . -name '*.py' -exec autopep8 --verbose --in-place --aggressive {} \;
secure:
        bandit --verbose --recursive core/*.py main.py

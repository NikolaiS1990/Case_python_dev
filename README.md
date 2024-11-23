📂 Project Structure
.
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── Activate.ps1
│   ├── pip
│   ├── pip3
│   ├── pip3.10
│   ├── py.test
│   ├── pytest
│   ├── python -> python3
│   ├── python3 -> /usr/bin/python3
│   └── python3.10 -> python3
├── data
│   ├── data_from_user.json
│   └── permit_requirements.json
├── include
├── __init__.py
├── lib
│   └── python3.10
├── lib64 -> lib
├── load_data.py
├── main.py
├── __pycache__
│   ├── __init__.cpython-310.pyc
│   └── load_data.cpython-310.pyc
├── pyvenv.cfg
├── README.md
├── structure_approver.py
└── test
    ├── __init__.py
    ├── load_data_test.py
    └── __pycache__


# Jsonfile data

## size limits of structues

Max size is set according to Rødovre Municipality's webpage:
https://www.rk.dk/borger/bolig-og-byggeri/byggeri/foer-du-bygger/byggetilladelse-hvornaar-og-hvordan


# Dependencies
pytest-8.3.3
# 🌟 Overview
This is a demo app to show how building permit processesing can be automated

# 🚀 Features
A tool to evaluate whether the square foot of a structue is large enough
to require a building permit.

# 📂 Project Structure
.
├── data
│   ├── data_from_user.json
│   └── permit_requirements.json
├── __init__.py
├── lib64 -> lib
├── load_data.py
├── main.py
├── pyvenv.cfg
├── README.md
├── structure_approver.py
└── test
    ├── __init__.py
    ├── load_data_test.py

# 🛠️ Installation
## Dependencies
pytest-8.3.3

# 🖥️ Usage
```
python3 main.py
```

# 🧪 Testing
```
pytest test/load_data_test.py
```


# 📡 Data Source

Max size is set according to Rødovre Municipality's webpage:
https://www.rk.dk/borger/bolig-og-byggeri/byggeri/foer-du-bygger/byggetilladelse-hvornaar-og-hvordan

The user_data is made up.



# 📜 License

This project is licensed under the MIT License.


# 📧 Contact
Email: nikolaisandbeck1990@gmail.com
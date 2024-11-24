"""The main script for the program."""
from structure_approver import StructureApprover
from load_data import JSONLoader


def main():
    """Entry point for the script.

    This script initializes a StructureApprover object, updates
    its permit requirements settings and give the user an evaluation of wether
    the structure requires a permit or not.

    It initializes the JSONLoader and parses the data from the JSON files
    to the methods from the StructureApprover class.

    Inputs:
        - None. All parameters are hardcoded in this example.

    Outputs:
        - Prints evaluation to the terminal.

    Usage:
        Run this script directly using Python:
            $ python3 main.py
    """

    # Load the permit requirements
    data_load = JSONLoader()
    permit_requirements = data_load.load_json("data/permit_requirements.json")
    user_data = data_load.load_json("data/data_from_user.json")

    structure_approver = StructureApprover()

    # Setting the permit requirements
    structure_approver.set_permit_requirements(permit_requirements)
        # Setting the permit requirements
    structure_approver.set_structure_size(user_data)

    # structure_approver.compare_size_to_requirements()
    print(structure_approver.get_evaluation())

if __name__ == "__main__":
    main()

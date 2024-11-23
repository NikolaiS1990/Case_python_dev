"""
This module implements the StructureApprover class.

The StructureApprover class provieds methods for checking of the size of a structure
requires a building permit.

Class:
    - StructureApprover: A class to do approval processes for building projects.

Usage:
    - To demonstrate how manual steps in the approval process can be done automatically.

    Example:
        structure_approver = StructureApprover()
        structure_approver.set_permit_requirements(50)
        structure_approver.set_structure_size(46)
        structure_approver.get_maximum_size()
"""

class StructureApprover:
    """
    A class to do approval processes for building projects."""
    def __init__(self):

        self.__structure_size = 0
        self.__permit_requirement_data = 0

    def set_structure_size(self, structure_size: dict):
        """Updates the max size limit of the structure.

        Parameters:
            permit_requirements (dict): A dictionary containing the max size limit of the structure.

        Raises:
            ValueError: If the value in the dictionary is empty
        """

        if not structure_size["size_of_structure"]:
            raise ValueError("No data found.")

        self.__structure_size = structure_size["size_of_structure"]


    def set_permit_requirements(self, permit_requirements: dict):
        """Updates the max size limit of the structure.

        Parameters:
            permit_requirements (dict): A dictionary containing the max size limit of the structure.

        Raises:
            ValueError: If the value in the dictionary is empty
        """

        if not permit_requirements["max_number_of_square_meters"]:
            raise ValueError("No data found.")

        self.__permit_requirement_data = permit_requirements["max_number_of_square_meters"]

    def get_maximum_size(self):
        """Returns the max size limit of the structure."""
        return self.__permit_requirement_data
    
    def get_structure_size(self):
        """Returns the max size limit of the structure."""
        return self.__structure_size


    def compare_size_to_requirements(self) -> bool:
        """Compares structure size to permit requirements."""
        if self.__structure_size > self.__permit_requirement_data:
            return False
        else:
            return True

    def get_evaluation(self) -> str:
        """Returns an evaluation of the structure size."""
        if self.compare_size_to_requirements():
            return f"The structure is smaller than {self.__permit_requirement_data}㎡. No permit required."

        return f"The structure is larger than {self.__permit_requirement_data}㎡. Permit required."

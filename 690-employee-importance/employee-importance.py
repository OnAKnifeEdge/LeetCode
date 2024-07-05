"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        e = {e.id: e for e in employees}
        employee = e[id]

        importance = employee.importance

        for sub in employee.subordinates:
            importance += self.getImportance(employees, sub)

        return importance
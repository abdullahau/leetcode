# https://leetcode.com/problems/rename-columns/

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id': 'student_id', 
                                    'first': 'first_name', 
                                    'last': 'last_name', 
                                    'age': 'age_in_years'})

if __name__ == "__main__":
    students = pd.DataFrame({
        "id": [1,4234,3,42],
        "first": ["123", '123','12313','12313'],
        "last": ["123", '123','12313','12313'],
        "age": [1,2,3,4]
    })
    
    print(renameColumns(students))
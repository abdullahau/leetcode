# https://leetcode.com/problems/modify-columns

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

if __name__ == "__main__":
    employees = pd.DataFrame({
        'name':['Jack', 'Piper', 'Mia', 'Ulysses'],
        'salary': [19666, 74754, 62509, 54866]
    })
    
    print(modifySalaryColumn(employees))
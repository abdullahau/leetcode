# https://leetcode.com/problems/create-a-dataframe-from-list/description/

import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])


if __name__ == "__main__":
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]

    print(createDataframe(student_data))
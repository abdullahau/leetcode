# https://leetcode.com/problems/method-chaining/

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

if __name__ == "__main__":
    animals = pd.DataFrame({
        'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
        'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
        'age': [90, 50, 6, 45, 100, 26],
        'weight': [464, 41, 328, 463, 50, 349]
    })
    
    print(findHeavyAnimals(animals))
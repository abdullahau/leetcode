# https://leetcode.com/problems/get-the-size-of-a-dataframe/

import pandas as pd

# def getDataframeSize(players: pd.DataFrame) -> list[int]:
#     return [len(players.index), len(players.columns)]

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

if __name__ == "__main__":
    players = pd.DataFrame({
        'player_id': [123, 213, 123, 545, 643, 654],
        'name': ['dsf', 'dsfs', 'dfs', 'fsdf', 'dfds', 'cvbcv']
    })
    
    print(getDataframeSize(players))
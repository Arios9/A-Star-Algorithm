import pandas as pd
import math


data = [
    (5, 0, 5, None),
    (math.inf, math.inf, 7, None),
    (math.inf, math.inf, 3, None),
    (math.inf, math.inf, 4, None),
    (math.inf, math.inf, 0, None),
    (math.inf, math.inf, 6, None),
    (math.inf, math.inf, 5, None),
    (math.inf, math.inf, 6, None)
]

df = pd.DataFrame.from_records(
    data=data,
    columns=['Fscore', 'Gscore', 'heuristic', 'lastNode']
)

connections = [
    (0, 1, 5),
    (0, 2, 9),
    (0, 4, 6),
    (1, 2, 3),
    (1, 7, 9),
    (2, 1, 2),
    (2, 3, 1),
    (3, 0, 6),
    (3, 7, 5),
    (3, 6, 7),
    (4, 3, 2),
    (4, 5, 2),
    (5, 7, 7),
    (6, 4, 2),
    (6, 7, 8)
]

connections_df = pd.DataFrame.from_records(
    data=connections,
    columns=['from', 'to', 'cost']
)

def reconstruct_path(current):
    path = []
    while current is not None:
        path.insert(0, current)
        current = df.at[current, 'lastNode']
    return path

def A_Star(start, goal):
    openSet = [start] 
    while openSet:
        current = df.loc[openSet, :]['Fscore'].idxmin()
        if(current == goal): return reconstruct_path(current)
        openSet.remove(current)
        current_connections = connections_df[connections_df['from'] == current].to_dict('records')
        for connection in current_connections:
            tentative_gScore = df.loc[current, 'Gscore'] + connection['cost']
            if(tentative_gScore < df.loc[connection['to'], 'Gscore']):
                df.at[connection['to'], 'lastNode'] = current
                df.at[connection['to'], 'Gscore'] = tentative_gScore
                df.at[connection['to'], 'Fscore'] = tentative_gScore + df.at[connection['to'], 'heuristic'] 
                if connection['to'] not in openSet:
                    openSet.append(connection['to'])
    return []



print(A_Star(0, 7))













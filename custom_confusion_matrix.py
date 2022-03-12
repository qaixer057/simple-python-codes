import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
'''
Define array as your results and rename the train list as per your classes.
Diagnoal Enteries are correct results other are wrong results.
'''
array = [[13,1,1,0,2],
         [3,9,6,0,1],
         [0,0,16,2,0],
         [0,0,0,13,0],
         [0,0,0,0,15]]
train = ['Normal', 'DoS', 'Probe', 'U2R', 'R2L']
df_cm = pd.DataFrame(array, train, train)
# df_cm = pd.DataFrame(array, range(5), range(5))
# plt.figure(figsize=(10,7))
sn.set(font_scale=1.4) # for label size
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size
plt.show()

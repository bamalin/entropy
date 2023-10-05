import os
import pandas as pd

df = pd.read_excel("D:/PhD/Entropy/PCB-P/PCB-P Pers Rot Grayscale Histogram Flattened No Norm.xlsx")
class_hist_list = []

for board in df[1].unique():
    board_df = df[df[1]==board]
    i=3
    class_list = [board]
    avg = board_df[3].mean()
    while i < board_df.shape[1]-1:
        avg = board_df[i].mean()
        class_list.append(avg)
        i+=1
    class_hist_list.append(class_list)
df = pd.DataFrame(class_hist_list)
df.to_excel("D:/PhD/Entropy/PCB-P/PCB-P Grayscale Histogram Flattened No Norm Perspective Averages.xlsx")



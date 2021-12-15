import matplotlib.pyplot as plt
import numpy as np

dataPath = "data/"
dataFile = "10_ShapeDimExp_2021_Dec_01_1445.csv"

rawData = []
with open(dataPath + dataFile, "r") as file:
    fileRow = file.readline()
    while fileRow != "":
        #print(fileRow)
        rawData.append(fileRow.strip().split(","))
        fileRow = file.readline()

onsetInd = 20
corRespInd = 3
respInd = 18
rtInd = 19

onsets = [(row[onsetInd]) for row in rawData[1:]]
corResps = [row[corRespInd].lower() for row in rawData[1:]]
resps = [row[respInd] for row in rawData[1:]]
RTs = [round((row[rtInd]),3) for row in rawData[1:]]

goodRTs = []
goodOnsets = []
#to loop over every trial
for i in range(0,40):
    if resps[i] == corResps[i]:
            goodRTs.append(RTs[i])
            goodOnsets.append(onsets[i])
    else:
        print("Error trial at:", i)

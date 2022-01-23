import random
import plotly.figure_factory as pf
import pandas
import statistics as s

df = pandas.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

populationMean = s.mean(data)
print("popuation mean : " , populationMean)

def random_set_of_mean(counter):
    dataSet = []
    for a in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataSet.append(value)

    mean = s.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = s.mean(df)
    print("samplingMean : " , mean)
    fig = pf.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans = random_set_of_mean(30)
        meanList.append(setOfMeans)
    showFig(meanList) 

setup()
#generates sample performance plots (1 month, 1 year, 3 year, 5 year)
#uses randomly generated data
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

def generateData1():
    time = 52 * 5 * 5 # 5 years of returns with daily timeStep
    dailyReturn = np.random.normal(1.00075, 0.01, time) #daily percent return (with .1 = 10%)
    makePlot(dailyReturn, 0, time, './images1/five_year_performance')
    makePlot(dailyReturn,2/5*time, time, './images1/three_year_performance')
    makePlot(dailyReturn, 4/5*time,  time, './images1/one_year_performance')
    makePlot(dailyReturn, time-25, time, './images1/one_month_performance')

def generateData2():
    time = 52 * 5 * 5 # 5 years of returns with daily timeStep
    dailyReturn = np.random.normal(1.0005, 0.003, time) #daily percent return (with .1 = 10%)
    makePlot(dailyReturn, 0, time, './images2/five_year_performance')
    makePlot(dailyReturn, 2/5*time, time, './images2/three_year_performance')
    makePlot(dailyReturn,4/5*time,  time, './images2/one_year_performance')
    makePlot(dailyReturn,time-25, time, './images2/one_month_performance')

def makePlot(returns, first, last, output_file):
    first = int(first)
    last = int(last)
    initialCash = 10000

    cashData = [initialCash] * (last-first)

    for i in range(1, last-first):
        cashData[i] = cashData[i-1] * returns[i+first]


    plt.plot(cashData, 'g-')
    plt.xlabel('Market days since start')
    plt.ylabel('Current value')
    plt.title("Growth of $10,000 Initial Investment")
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(tick)  

    plt.tight_layout()
    
    plt.savefig(output_file)
    plt.close()

time = 52 * 5 * 5 # 5 years of returns with daily timeStep
dailyReturn = np.random.normal(1.0008, 0.001, time) #daily percent return (with .1 = 10%)

generateData1()
generateData2()


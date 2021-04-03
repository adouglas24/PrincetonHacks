#approach inspired from https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f
import matplotlib.pyplot as plt

def firstPie():
    labels = 'Technology', 'Energy', 'Agriculture', 'Financials'
    sizes = [37.1, 28.2, 15.7, 19]
    explode = (0.03, 0.03, 0.03, 0.03) 

    colors = ['#3137FD','#50FFB1','#DBD4D3','#ED6A5A']

    plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images1/piechart")
    plt.close()

def secondPie():
    labels = 'Technology', 'Financials'
    sizes = [99.1, 0.9]
    explode = (0.03, 0.03) 

    colors = ['#3137FD','#50FFB1']

    plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images2/piechart")
    plt.close()


firstPie()

secondPie()
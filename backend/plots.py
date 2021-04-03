#approach inspired from https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f
#generates the figures for algorithms -- the pie charts and rating scales
import matplotlib.pyplot as plt

def first_pie():
    labels = 'Technology', 'Energy', 'Agriculture', 'Financials'
    sizes = [37.1, 28.2, 15.7, 19]
    explode = (0.03, 0.03, 0.03, 0.03) 

    colors = ['#50FFB1', '#3137FD','#DBD4D3','#ED6A5A']

    plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images1/piechart")
    plt.close()

def second_pie():
    labels = 'Technology', 'Financials'
    sizes = [99.1, 0.9]
    explode = (0.03, 0.03) 

    colors = ['#50FFB1', '#3137FD']

    plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images2/piechart")
    plt.close()

def a_plus():
    sizes = [100]

    colors = ['#00bf00']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images1/a_plus_raw")
    plt.close()


def f():
    sizes = [100]

    colors = ['#e60207']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images2/f_raw")
    plt.close()

def a_minus():
    sizes = [80, 20]

    colors = ['#00bf00', '#ffffff']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images2/a_minus_raw")
    plt.close()


def b_plus():
    sizes = [70, 30]

    colors = ['#00bf00', '#ffffff']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images1/b_plus_raw")
    plt.close()


def b():
    sizes = [65, 35]

    colors = ['#00bf00', '#ffffff']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images2/b_raw")
    plt.close()


def d():
    sizes = [65, 35]

    colors = ['#e60207', '#ffffff']

    plt.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, shadow=True)

    centre_circle = plt.Circle((0,0),0.90,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()

    plt.savefig("./images1/d_raw")
    plt.close()


first_pie()

second_pie()

a_plus()

f()

a_minus()

b_plus()

b()

d()
#John Rugan
#Some cheeky speculation in statistics


import PySimpleGUI as sg
import matplotlib.pyplot as plt


def plot_graph(p, n):
    x = list(range(1, n + 1))
    cdf_values = [cdf(p, i) for i in x]
    pmf_values = [pmf(p, i) for i in x]

    plt.figure(figsize=(8, 6))
    plt.bar(x, cdf_values, width=0.4, label="CDF", align='center', color='blue', alpha=0.7)
    plt.bar(x, pmf_values, width=0.4, label="PMF", align='edge', color='orange', alpha=0.7)
    plt.xlabel("Number of Trials")
    plt.ylabel("Probability")
    plt.title("Cumulative Density Function (CDF) and Probability Mass Function (PMF)")
    plt.legend()
    plt.grid(True)
    plt.xticks(x)
    plt.show()


#creating multiline outside of layout to name it
logwindow = sg.Multiline(size=(30, 10), key='textbox')

#Entire window layout here
layout = [[sg.Text("Cumulative Density Function of Geometric distribution")], 
          [sg.Text("Probability"), sg.Push(), sg.InputText(size=(5, 1),key='probbox')],
          [sg.Text("Number of trials"), sg.Push(), sg.InputText(size=(5, 1),key='trialbox')],
          [sg.Checkbox("Progression",key='prog'),logwindow],
          [sg.Button("OK"),sg.Button("Show Graph"),sg.Button("Close")]]

#Geometric Distribution Functions
#Cumulative Density Function
cdf = lambda a, b : 1 - ((1 - a)**(b)) #P(X <= x) Probability that first success is within those amount of trials
#Probability Mass Function
pmf = lambda a, b : ((1-a)**(b-1))*a #P(X = x) Probability that first success is exacty x amount of trials

# Create the window
window = sg.Window("GeoDistribution", layout,element_justification='r')



# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window or
    # presses the OK button
    if event == "OK" and values['probbox'] and values['trialbox']:
        logwindow.Update('')

        p = float(values['probbox'])
        n = int(values['trialbox'])

        logwindow.print(f"Probability that first success is within {n} trials:")
        logwindow.print("\nP(X<=x)",round(cdf(p,n),5))
        logwindow.print("P(X=x)",round(pmf(p,n),5))
        

        if values['prog'] == True:
            logwindow.print(f"\nProgression of CDF to {n} trials\n")
            for x in range(n):
                logwindow.print(x+1,round(cdf(p,x+1),5))


        logwindow.print("\nμ =",round(((1-p)/p),5)," σ^2 =",round(((1-p)/(p**2)),5))

    if event == "Show Graph" and values['probbox'] and values['trialbox']:
        p = float(values['probbox'])
        n = int(values['trialbox'])
        plot_graph(p, n)

    if event == "Close" or event == sg.WIN_CLOSED:
        break



window.close()

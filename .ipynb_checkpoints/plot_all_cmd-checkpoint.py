import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('default')
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
plt.rcParams['font.size'] = 30

Cluster_ID=[104,362,3201,4833,5139,6121,6218,6254,6362,6397,6656,6752,6809,6838]

for CID in Cluster_ID:
    plt.figure(figsize=[10,10])
    cluster_name = "ngc"+str(CID)
    #plt.gca().invert_yaxis()
    Color,App = np.loadtxt("Data/"+cluster_name+".dat",unpack = True)
    plt.scatter(Color,App,s=1.6,c="purple",alpha=0.5)
    #plt.xlim(-0.5,2)
    plt.xlabel("$f606w - f814w$")
    plt.ylabel("$f606w$")
    plt.axis([-0.2,1.5,25,13])
    plt.title("NGC "+str(CID))
    #plt.legend(loc=3, prop={'size': 12})
    plt.savefig("Figures/HR/"+cluster_name+".pdf")
    
print("Figures saved!")

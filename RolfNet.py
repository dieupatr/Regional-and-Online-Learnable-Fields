from math import *
import pickle

def Distance(P,Q):
    
    if len(P)==len(Q):
        return sqrt(sum([(P[k]-Q[k])**2  for k in range(len(P)) if P[k]!=None and Q[k]!=None  ]))
    return "Error missmath lenght"

def MeanRadius( Neurons):

    Mean=0

    if len(Neurons)==0:
        return 1

    for idn in Neurons:

         sigma=Neurons[idn][1]

         Mean=Mean+sigma

    return Mean

# Find the next Neuron with the shortest distance to the in put x
# input:
# x sampel
# Neurons set of Neurons
# rho constant
# valid +
def FindNextNeuron( x , Neurons, rho ):

    BestNeuron="none"
    ShortDis=100000

    if len(Neurons)==0:
        return [ BestNeuron, ShortDis ]
        
    for idn in  Neurons:

        ck=Neurons[idn][0]
        sigma=Neurons[idn][1]
        dis=Distance(ck,x)


        if dis<=rho*sigma and dis<=ShortDis :
            
            BestNeuron=idn
            ShortDis=dis

    return [ BestNeuron, ShortDis ]


# Chnage the position of the neurons or place a new one
# input:
# x sampel
# Neurons set of Neurons
# rho constant
# etac, etas  learning rate
# Valid +
def ChangeNeurons(Neurons, x ,rho, etac, etas):

    [idn, dis]=FindNextNeuron( x , Neurons, rho )
    N=len(Neurons)

    if idn=="none" and dis==100000:
        
        sigma0=MeanRadius( Neurons)
        Neurons[f"{N}"]=[x, sigma0]
        
    else:
        
        ck=Neurons[idn][0]
        sigma=Neurons[idn][1]
        
        Neurons[idn][0]=[ ck[k]*(1-etac)+x[k]*etac for k in range(len(x))   ]
        Neurons[idn][1]=sigma*(1-etas)+etas*dis

##########    
def TrainModell(Neurons, Sampels, rho, etac, etas, Nrun ):

    for k in range(Nrun):
        for x in Sampels:
            ChangeNeurons(Neurons, x ,rho, etac, etas)




###########Manage Model#############

def StoreModel(Neurons, rho,etac, etas,Nrun,info, file):

    Parameter={

    "rho" :rho,
    "etac": etac,
    "etas": etas,
    "Nrun": Nrun

    }
    Model={

        "Neurons": Neurons,
        "Parameter": Parameter,
        "info": info

        }
    
    with open(file, 'wb') as file:
        pickle.dump(Model, file)

    

def LoadModel(filename):

    with open(filename,'rb') as file: Model=pickle.load(file)
    return Model




def MakePrediction(Model,x):
    [idn, dis]=FindNextNeuron(x ,
                               Model["Neurons"],
                               Model["Parameter"]["rho"]     
                               )
    
    return Model["Neurons"][idn][0]

    









            





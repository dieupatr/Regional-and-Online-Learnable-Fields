from RolfNet import *


###########  Definition Model ###########

Neurons={    }
rho=1
etac, etas=0.1,0.005
Nrun=100
info="""

Test model to check workflow

"""

########    Data to Train ###########

#  Represent the logic AND

Sampels=[
          [0,0,0],
          [1,1,1],
          [1,0,0],
          [0,1,0]
        ]

########  Train Model #####


TrainModell(Neurons, Sampels, rho, etac, etas, Nrun )


###########Save Model###########################
    
file="TestModel.pkl"
StoreModel(Neurons, rho,etac, etas,Nrun,info, file)


######## Load Model #############
Model=LoadModel(file)
x=[1,1,None]

print(MakePrediction(Model,x) )




    

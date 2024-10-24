import numpy as np

class Matrix:
    def __init__(self, Mat1=None, Mat2=None):
        self.Mat1=np.array(Mat1)
        self.Mat2=np.array(Mat2)

    def addition(self):
        if np.shape(self.Mat1)==np.shape(self.Mat2):
            result=self.Mat1+self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def subtraction(self):
        if self.Mat1.shape==self.Mat2.shape:
            result=self.Mat1-self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def Mult(self):
        if self.Mat1.ndim==self.Mat2.ndim and self.Mat1.shape[1]==self.Mat2.shape[0]:
            result=self.Mat1@self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def inverse(self):
        
    
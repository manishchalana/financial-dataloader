import os, time
import pandas as pd



class DataLoader:
    def __init__(self, direcPath, fileNamesTrain, fileNamesTest, attributeNamesTrain=None, attributeNamesTest=None):
        self.test_vars = len(fileNamesTest)
        self.train_vars = len(fileNamesTrain)
        self.prepareData(direcPath, fileNamesTrain, fileNamesTest, attributeNamesTrain, attributeNamesTest)
        
    
    def prepareData(self, direcPath, fileNamesTrain, fileNamesTest, attributeNamesTrain=None, attributeNamesTest=None):
        attributeNamesTrain = self.setAttributeNames(fileNamesTrain, attributeNamesTrain)
        attributeNamesTest = self.setAttributeNames(fileNamesTest, attributeNamesTest)
        
        self.checkValidDirectory(direcPath)
        self.checkValidFiles(direcPath, fileNamesTrain + fileNamesTest)
        self.checkValidAttributeNames(fileNamesTrain, attributeNamesTrain)
        self.checkValidAttributeNames(fileNamesTest, attributeNamesTest)
        
        dataFiles = fileNamesTrain + fileNamesTest
        attributes = attributeNamesTrain + attributeNamesTest
        
        try:
            
            dfList = [pd.melt(pd.read_csv(os.path.join(direcPath, dataFiles[i] + ".csv"), parse_dates=['Dates']), id_vars=['Dates'], var_name="Ticker", value_name= attributes[i]).set_index(["Ticker", "Dates"]) for i in range(len(dataFiles))] #

            self.data =  pd.concat(dfList, axis=1)
            print("Data successfully read")
            
        except:
            print("Data not read")
            

            
    def generateDataByStock(self):

        
        for stock, group in self.data.groupby(level=0):
            yield stock, group
            
    def checkValidDirectory(self, direcPath):
        assert os.path.isdir(direcPath), "The given path does not correspond to a directory."
    
    def checkValidAttributeNames(self, fileNames, attributeNames):
        assert len(attributeNames) == len(fileNames), "The file names and corresponding headers are not of equal length. System will exit here."
        assert len(attributeNames) == len(set(attributeNames)), "Duplicate attribute names found"
        
    def checkValidFiles(self, direcPath, fileNames):
        assert set([os.path.isfile(os.path.join(direcPath, file + ".csv")) for file in fileNames])=={True}, "Please make sure the filenames are valid files."
    
    def setAttributeNames(self, fileNames, attributeNames):
        if attributeNames is None:
            attributeNames = fileNames
        return attributeNames



    def generateRollingData(self, dataArray,  numPoints=250):
        for i in range(dataArray.shape[0]-numPoints):
            yield i+1, dataArray.iloc[i:(i + numPoints), :]
            
            
if __name__ =="__main__":

  direcPath = r"D:\Work\Research\data"
  fileNamesTrain = ['fopen', 'fhigh', 'flow', 'futoi1', 'futvol1']
  attributeNamesTrain = ""
  fileNamesTest= ['future_returns_close']
  attributeNamesTest = ['close_returns']
  numRollingDataPoints = 250    
  output = r"D:\Work\Research\output.xlsx"
  
  dl = DataLoader(direcPath, fileNamesTrain, fileNamesTest, attributeNamesTest=attributeNamesTest)

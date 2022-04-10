
import pandas as pd

class File():
   
    def __init__(self, nomefile):
        self.nomefile = nomefile
        
        
    def getCollumns(self):
        
        file = pd.read_csv(self.nomefile)
        df = pd.DataFrame(file)
        return df.columns.values
        
    def getDataFrame(self):
        file = pd.read_csv(self.nomefile)
        df = pd.DataFrame(file)
        return df
    
    def getAllStructOfCsv(self):
        
        file = pd.read_csv(self.nomefile)
        df = pd.DataFrame(file)
        colunas = df.columns.values
        data = []
        for iterador in range(len(df)):
            aux = []
            for coluna in colunas:
                item = df.loc[iterador,[coluna]][0]
                aux.append((coluna,item))
                
            data.append(aux)
        return data
    
from files import *

if __name__ == "__main__":
    
    file = File('WineQT.csv')
    lista = file.getAllStructOfCsv()
    data = []

    for item in lista:
        for subitem in item:
            if subitem[0] == 'quality':
                if subitem[1] > 7.5:
                    data.append(item)
                    
    fixed_acidity = []
    volatile_acidity = []
    citric_acid = []
    residual_sugar = []
    chlorides = []
    free_sulfur_dioxide = []
    total_sulfur_dioxide = []
    density = []
    pH = []
    sulphates = []
    alcohol = []
    quality = []
    Id = []                  
    
    for item in data:
        for subitem in item:
            coluna = subitem[0]
            value  = subitem[1]
            if coluna == 'fixed acidity':
                fixed_acidity.append(value)
            elif coluna == 'volatile acidity':
                volatile_acidity.append(value)
            elif coluna == 'citric acid':
                citric_acid.append(value)
            elif coluna == 'residual sugar':
                residual_sugar.append(value)
            elif coluna == 'chlorides':
                chlorides.append(value)
            elif coluna == 'free sulfur dioxide':
                free_sulfur_dioxide.append(value)
            elif coluna == 'total sulfur dioxide':
                total_sulfur_dioxide.append(value)
            elif coluna == 'density':
                density.append(value)
            elif coluna == 'pH':
                pH.append(value)
            elif coluna == 'sulphates':
                sulphates.append(value)
            elif coluna == 'alcohol':
                alcohol.append(value)
            elif coluna == 'quality':
                quality.append(value)
            elif coluna == 'Id':
                Id.append(value)
                
    obj = {
        'fixed acidity' : fixed_acidity,
        'volatile acidity' : volatile_acidity,
        'citric acid' : citric_acid,
        'residual sugar' : residual_sugar,
        'chlorides' : chlorides,
        'free sulfur dioxide' : free_sulfur_dioxide,
        'total sulfur dioxide' : total_sulfur_dioxide,
        'density' : density,
        'pH' : pH,
        'sulphates': sulphates,
        'alcohol' : alcohol,
        'quality' : quality,
        'Id' : Id
    }
    
    newDf = pd.DataFrame(obj)
    print(newDf)
    newDf.to_csv('NewWine.csv')
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'MSSubClass':1,'MSZoning':2,'Neighborhood':3,'OverallQual':4,'YearRemodAdd':5,'RoofStyle':6,'BsmtQual':7,'BsmtExposure':8,'HeatingQC':9,'CentralAir':10,'1stFlrSF':11,'GrLivArea':12,'BsmtFullBath':13,'KitchenQual':14,'Fireplaces':15,'FireplaceQu':16,'GarageType':17,'GarageFinish':18,'GarageCars':19,'PavedDrive':20,'SaleCondition':21})
print(r.json())
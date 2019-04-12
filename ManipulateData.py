'''
Created on 10. apr. 2019

@author: Lars Jespersen
@contains: functions to create, update and delete products in unisport sample data 
'''

class ManipulateData(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def deleteProductById(self, oUnisportData, iDeleteId):  
        try:
            oDataList = oUnisportData['products']       
            for i in oDataList:
                if int(i['id'])==iDeleteId:
                    oDataList.remove(i)
                    break
            return oDataList
        except:
            print('An error have occured')    
            
    def updateProductById(self,oUnisportData, iUpdateId, sUpdateKey, sUpdateValue):
        try:
            oDataList = oUnisportData['products']       
            for i in oDataList:
                if int(i['id'])==iUpdateId:
                    i[sUpdateKey]=sUpdateValue + i[sUpdateKey] 
                    break
            return oDataList
        except:
            print('An error have occured')       
            
    def createProduct(self,oUnisportData, oNewProduct):
        try:
            oUnisportData['products'].append(dict(oNewProduct[0]))                 
            return oUnisportData
        except:
            print('An error have occured')
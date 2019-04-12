'''
Created on 9. apr. 2019

@author: Lars Jespersen
@contains: functions for sorting the data fetched from unisport sample data or other sources
'''

class SortData(object):

    def __init__(self):
        '''
        Constructor
        '''
        
    def sortByPrice(self, oUnisportData, bSortOrder):
        try:
            oDataList = oUnisportData['products']
            oSortedList = sorted(oDataList, key = lambda i: int(i['price']),reverse=bSortOrder)
            return oSortedList
        except:
            print('An error have occured')   

    def getSpecificDictById(self,oUnisportData,iProductId):
        try:
            oDataList = oUnisportData['products']        
            # loop data until dict is found, then stop and return to make search faster
            oDict = None
            for i in oDataList:
                if int(i['id']) == iProductId:
                    oDict = i                
                    break
            return oDict      
        except:
            print('An error have occured')
            
    def getDictsByStringInKeyValue(self,oUnisportData,sTestKey,sTestValue):
        try:
            oDataList = oUnisportData['products']       
            oReturnList = []
            oDict = None
            for i in oDataList:
                sKey=i[sTestKey]
                if sKey.find(sTestValue)!=-1:
                    oDict = i                
                    oReturnList.append(dict(oDict))
                    
            oSortedList = sorted(oReturnList, key = lambda j: int(j['price']),reverse=False)
            return oSortedList 
        except:
            print('An error have occured') 
            
    def paginateList(self,oList,oPageNumber,oPrPage):
        iStartPos=(int(oPageNumber)*oPrPage)-oPrPage
        oPage= oList[iStartPos:iStartPos+oPrPage]    
        return oPage
    
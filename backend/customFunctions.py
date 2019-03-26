import accessDbs_Api



def totalSpendCategory(customerId):
    '''negative value means money is spent, positive value means money is got'''
    moneyIn=0
    for account in accessDbs_Api.depositAccList(customerId):
        Id = account["accountId"]
        d={}
        for transaction in accessDbs_Api.transactionDetails(Id, '01-01-2018','02-01-2019'): # for example
            if transaction['tag'] not in d.keys():
                d[transaction['tag']]=0

            if transaction["type"]=="DEBIT":
                d[transaction['tag']]-= float(transaction['amount'])
            elif transaction["type"]=="CREDIT":
                d[transaction['tag']]+= float(transaction['amount'])
                        
            d[transaction['tag']]+=moneyIn
    
    return d

def avgMonthly(customerId):
    avg=0
    for account in accessDbs_Api.depositAccList(customerId):
        Id = account["accountId"]
        for month in range(1,13):
            try:
                x=float(accessDbs_Api.depositAccBalance(Id, month, 2018)['availableBalance'])
                avg+=x
            except:pass
    
    return avg/12

# print(totalCredit(1))
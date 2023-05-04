# stock-price-Analysis
collects the stocks symbol and the date it triggered ,using python yfinance library i have been collecting the stock price of that stock using symbol and finding the change in the price each day and ultimately finding the best stocks which gives the best profits using sort and writing this data into excel for easy reading and access
from datetime import date,datetime, timedelta
import datetime
from collections import defaultdict
import csv
import yfinance as yf


def date_format(string):
    date=''
    temp=''
    for i in string:
        if i=="-":
            date+=temp[::-1]+i
            temp=''
        else:
            temp+=i
    date+=temp[::-1]
    return date

print('-------------------------------------------')

#to read csv file

with open('C:\python\stocksproject.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_stocks=[]
    for line in csv_reader:
        list_stocks.append([line[0],line[1],line[2],line[3]])

#to add data in csv to dictionary 
        
    symbol={}
    for line in list_stocks[1:]:
        string=line[0]
        string=string[::-1]
        date=date_format(string)
        try:
            symbol[line[1]].append(date)
        except:
            symbol[line[1]]=[date]
    print(symbol)
    
    
    Dates=[]

 #---------------------------------------------------

 # geeting the timestamp for which we needed
 
    start_date = datetime.date(year=2022, month=5, day=1)
    end_date = datetime.date(year=2023, month=5, day=1)
    
    current_date = start_date
    while current_date < end_date:
        date,day=current_date.strftime('%Y-%m-%d'), current_date.strftime('%A')
        if day not in ['Saturday','Sunday']:
            Dates.append(date)
        current_date += datetime.timedelta(days=1)


    today=datetime.date.today()
    

    days=len(Dates)

    #-----------------------------------------------

    #writing the first row in the csv file
    
    data=[[]*1]
    data[0].append("symbol")
    for j in Dates:
        data[0].append(str(j))
        data[0].append("change")
        
    filename = "stockProjectdata.csv"
    mode = "w"
    with open(filename, mode, newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    

    #-------------------------------------------------------------
    
    symbol_info={}
    for i in symbol:
        symbol_info[i]=[0]*(2*days)
    list_of_all=[]
    for i in symbol:
        ticketsymbol=str(i)
        ticketsymbol+='.NS'
        tickerData=yf.Ticker(ticketsymbol)
        start=0
        print(i)
        for j in range(days):

            #-----------------------------------------
            if symbol[i][0]<=Dates[j]:
        
                curr=Dates[j]
            else:
                continue
                
            date_obj = datetime.datetime.strptime(curr, '%Y-%m-%d')

            # add one day to the date using timedelta
            
            next_day_obj = date_obj + datetime.timedelta(days=1)

            # convert the result back to a string
            
            next_day = next_day_obj.strftime('%Y-%m-%d')

            
            #--------------------------------------------
            
            tickerDf=tickerData.history(period="1d", start=curr ,end= next_day)
            closed=tickerDf.loc[:, "Close"]
            
            try:
                closed=round(closed[-1],2)
                print(closed)
                if start==0:
                    start=closed
            except:
                closed=0
            if closed==0:
                symbol_info[i][2*j]='-'
            else:
                symbol_info[i][2*j]=closed 
            if start==0:
                change=0
            else:
                if closed!=0:
                    change=((float(closed)-start)/start)*100
                    change=round(change,2)
            symbol_info[i][2*j+1]=change
        print(symbol_info[i])
        list_of_all.append([symbol_info[i][-1],i])
        

            
        

    #-----------------------------------------------
    # to write data in csv file in sorted order
        
    list_of_all.sort()
    list_of_all=list_of_all[::-1]
    print(list_of_all)
    for i in list_of_all:
        data=[]
        symb=i[1]
        data.append([symb])
        data[0]+=symbol_info[symb]
        mode = "a"
        with open(filename, mode, newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)


    print("Data written successfully to the CSV file!")
        
    
        

    
    
        

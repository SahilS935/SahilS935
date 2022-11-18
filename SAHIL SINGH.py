print()
print("WELCOME TO RAILWAY RESERVATION PROJECT")

name: str = str(input("ENTER USERNAME : "))
if name == "sahil_singh".lower():
    print("RECORD FOUND FOR GIVEN USERNAME")
else:
    print("NO RECORDS")

password= input("ENTER PASSWORD : ")
if password == "sahilsingh":
   print("THANK YOU FOR LOGIN")
else:
       print("NO RECORDS")



import pandas as pd
import matplotlib.pyplot as plt

def menu():


    print ()
    print("A PROJECT ON RAILWAY RESERVATION SYSTEM")
    print()
    print("0. ABOUT THE PROJECT")
    print("1. DETAILS OF ALL TRAINS")
    print("2. SCHEDULE OF TRAINS")
    print("3. ADD NEW TRAIN DETAILS")
    print("4. NUMBER OF SEATS AVAILABLE")
    print("5. TRAIN ENQUIRY")
    print("6. CANCEL TRAIN")
    print("7. DELAY IN ARRIVAL")
    print("8. PASSENGERS DETAILS")
    print("9. ADD NEW PASSENGER DETAILS")
    print("10.TICKET RESERVATION")
    print("11.SHOW STATUS OF TICKETS")
    print("12.AC1 FARE OF ALL TRAINS GRAPH")
    print("13.AC2 FARE OF ALL TRAINS GRAPH")
    print("14.AC3 FARE OF ALL TRAINS GRAPH")
    print("15.SLEEPER FARE OF ALL TRAINS GRAPH")
    
    


menu()

def ABOUT_THE_PROJECT():
    print("A PROJECT ON RAILWAY RESERVATION SYSTEM BY SAHIL SINGH. IN THIS PROJECT WE HAVE USED CSV FILES. HERE, WE CAN SORT TRAINS,BOOK TICKETS,CANCEL TICKETS AND A LOT OF STUFFS.......")
    
    
def DETAILS_OF_ALL_TRAINS():
    print('HERE IS DETAILS OF ALL THE TRAINS')
    print()
    print()
    df=pd.read_csv("E:\TRAIN DETAILS.csv",index_col=0)
    print(df)
    
    
def SCHEDULE_OF_TRAINS():
    print('HERE IS SCHEDULE OF ALL THE TRAINS')
    print()
    print()
    df=pd.read_csv("E:\SCHEDULE OF TRAINS.csv",index_col=0)
    print(df)

def ADD_NEW_TRAIN_DETAILS():
    print ('ADD NEW TRAIN DETAILS')
    df=pd.read.csv("E:\TRAIN DETAILS.csv",index_col=0)
    print(df)
    a=int(input("ENTER TRAIN NUMBER : ")) 
    b=(input("ENTER TRAIN NAME: "))
    c=(input("ENTER SOURCE: "))
    d=(input("ENTER DESTINATION: "))
    e=int(input("ENTER AC_1 FARE: "))
    f=int(input("ENTER AC_2 FARE: "))
    g=int(input("ENTER AC_3 FARE: "))
    h=int(input("ENTER SLEEPER/CC FARE: "))
    df.loc[a]=[b,c,d,e,f,g,h]
    print(df)
    
def NUMBER_OF_SEATS_AVAILABLE():
    print('NUMBER OF SEATS AVAILABLE')
    print()
    print()
    df=pd.read_csv("E:\AVAILABILITY OF SEATS.csv",index_col=0)
    print(df)
    
    
def TRAIN_ENQUIRY():    
    print('ALL DETAILS OF AVAILABLE TRAINS')
    print()
    print()
    df=pd.read_csv("E:\TRAIN ENQUIRY.csv",index_col=0)
    print(df)
    
    
def CANCEL_TRAIN():    
    print('CANCELLING TRAIN DUE TO UNKNOWN REASONS')
    df=pd.read_csv("E:\TRAIN DETAILS.csv",index_col=0)
    print(df)
    TRAIN_NUMBER=int(input("ENTER TRAIN NUMBER. : "))
    df.drop(TRAIN_NUMBER,axis=0,inplace=True)
    print("TRAIN IS CANCELLED")
    print()
    print(df)
    
    
def DELAY_IN_ARRIVAL():
    print('TRAINS RUNNING DELAY')
    print()
    print()
    df=pd.read_csv("E:\TRAINS RUNNIND DELAYED.csv",index_col=0)
    print(df)
    
    
def PASSENGERS_DETAILS(): 
    print('DETAILS OF PASSENGERS')
    print()
    print()
    df=pd.read_csv("E:\PASSENGER DETAILS.csv",index_col=0)
    print(df)
    
    
def ADD_NEW_PASSENGER_DETAILS(): 
    print('ADDING NEW PASSENGERS DETAILS')
    df=pd.read_csv("E:\PASSENGER DETAILS.csv",index_col=0)
    print(df)
    n=(input("ENTER PASSENGER NAME : "))
    a=int(input("ENTER AGE : "))
    tn=int(input("ENTER TRAIN NO. : "))
    c=(input("ENTER CLASS : "))
    d=(input("ENTER DESTINATION : "))
    amt=int(input("ENTER AMOUNT : "))
    s=d=(input("ENTER STATUS: ")) 
    pnr=int(input("ENTER PNR NO, : "))
    df.loc[n]=[a,tn,c,d,amt,s,pnr]
    print(df)
    
    
def TICKET_RESERVATION():
    print("HERE ARE AVAILABLE SEATS :- ")
    print("TNUMBER IS 12557 FOR SAPT KRANTI EXPRESS FROM ANVT")
    print()
    print("1. AC1 COSTS 5600")
    print("2. AC2 COSTS 4500")
    print("3. AC3 COSTS 3995")
    print("4. NO TICKET IN SLEEPER")
    print()
    print("TNUMBER IS 23568 FOR JAN SHATABDI EXPRESS FROM NEW DELHI")
    print()
    print("1. AC1 COSTS 6000")
    print("2. AC2 COSTS 5100")
    print("3. AC3 COSTS 4100")
    print("4. SLEEPER COSTS 2990")
    print()
    print("TNUMBER IS 78643 FOR VANDE BHARAT EXPRESS FOR NEW DELHI")
    print()
    print("1. AC1 COSTS 7894")
    print("2. AC2 COSTS 6689")
    print("3. AC3 COSTS 5500")
    print("4. CHAIR CAR COSTS 4000")
    print()
    print("TNUMBER IS 65778 FOR TEJAS EXPRESS FROM NEW DELHI")
    print()
    print("1. TRAIN IS CANCELLED")
    print()
    print("TNUMBER IS 77456 FOR RAJDHANI EXPRESS FROM NEW DELHI")
    print()
    print("1. TRAINS DEPARTED")
    print()

    
    tname=(input("ENTER TRAIN NUMBER : "))
    print(tname)
    x=int(input("ENTER YOUR CHOICE OF CLASS : "))
    
    if(x==1):
        print("YOU HAVE CHOSEN AC1")
        s=5600
        
    if(x==2):
        print("YOU HAVE CHOSEN AC2")
        s=4500
        
    if(x==3):
        print("YOU HAVE CHOSEN AC3")
        s=3995

    if(x==4):
        print("SORRY ALL TICKETS ARE BOOKED")
        s=0
        
    else:
         print("INVALID RESPONSE")
         
         print("PLEASE CHOOSE A TRAIN")
         print("YOUR TOTAL TICKET PRICE IS = s ")
        
    
    if(x==1):
         print("YOU HAVE CHOSEN AC1")
         s=6000
         
    if(x==2):
         print("YOU HAVE CHOSEN AC2")
         s=5100
         
    if(x==3):
         print("YOU HAVE CHOSEN AC3")
         s=4100
         
    if(x==4):
         print("SORRY ALL TICKETS ARE BOOKED")
         s=2990
         
    else:
          print("INVALID RESPONSE")
          
          print("PLEASE CHOOSE A TRAIN")
          print("YOUR TOTAL TICKET PRICE IS = s") 
                
                
    if(x==1):
           print("YOU HAVE CHOSEN AC1")
           s=7894
           
    if(x==2):
           print("YOU HAVE CHOSEN AC2")
           s=6689
           
    if(x==3):
           print("YOU HAVE CHOSEN AC3")
           s=5500
           
    if(x==4):
           print("SORRY ALL TICKETS ARE BOOKED")
           s=4000
           
    else:
           print("INVALID RESPONSE")
            
           print("PLEASE CHOOSE A TRAIN")
           print("YOUR TOTAL TICKET PRICE IS = s")
            
                  
    if (x==1):
        print("TRAIN IS CANCELLED")
        
        
    else:
        print("TRAIN IS CANCELLED")
        
        
    if(x==1):
        print("TRAIN IS DEPRATED")
            
    else:
        print("TRAIN IS DEPARTED")
        
        
        
def SHOW_STATUS_OF_TICKETS():
     print("STATUS OF TICKETS") 
     df=pd.read_csv("E:\PASSENGER DETAILS.csv",usecols=['PASSENGER NAME','STATUS'])
     print(df)
     
     
def AC1_FARE_OF_ALL_TRAINS():
    print('AC1 FARE OF TRAINS')
    df=pd.read_csv("E:\AC1 FARE.csv") 
    x=df['TRAIN NAME']
    y=df['AC1']
    plt.title('AC1 FARE FOR TRAINS', fontsize=14,color="r")
    plt.xlabel("TRAINS",fontsize=14,color="r")
    plt.ylabel("AC1 FARE", fontsize=14,color="r")
    plt.plot(x,y,marker='X',color='g')
    plt.show()
    
    
def AC2_FARE_OF_ALL_TRAINS():
    print('AC2 FARE OF TRAINS')
    df=pd.read_csv("E:\AC2 FARE.csv") 
    x=df['TRAIN NAME']
    y=df['AC2']
    plt.title('AC1 FARE FOR TRAINS', fontsize=14,color="r")
    plt.xlabel("TRAINS",fontsize=14,color="r")
    plt.ylabel("AC2 FARE", fontsize=14,color="r")
    plt.plot(x,y,marker='X',color='g')
    plt.show()


def AC3_FARE_OF_ALL_TRAINS():
    print('AC3 FARE OF TRAINS')
    df=pd.read_csv("E:\AC3 FARE.csv") 
    x=df['TRAIN NAME']
    y=df['AC3']
    plt.title('AC1 FARE FOR TRAINS', fontsize=14,color="r")
    plt.xlabel("TRAINS",fontsize=14,color="r")
    plt.ylabel("AC3 FARE", fontsize=14,color="r")
    plt.plot(x,y,marker='X',color='g')
    plt.show()


def SLEEPER_FARE_OF_ALL_TRAINS():
    print('SLEEPER FARE OF TRAINS')
    df=pd.read_csv("E:\SLEEPER FARE.csv") 
    x=df['TRAIN NAME']
    y=df['SLEEPER']
    plt.title('SLEEPER FARE FOR TRAINS', fontsize=14,color="r")
    plt.xlabel("TRAINS",fontsize=14,color="r")
    plt.ylabel("SLEEPER FARE", fontsize=14, color="r")
    plt.plot(x, y, marker='X', color='g')
    plt.show()    
    
    

opt=int(input("ENTER YOUR CHOICE : "))

if opt==0:
   ABOUT_THE_PROJECT()
if opt==1:
   DETAILS_OF_ALL_TRAINS()
elif opt==2:
   SCHEDULE_OF_TRAINS()
elif opt==3:
   ADD_NEW_TRAIN_DETAILS()
elif opt==4:
   NUMBER_OF_SEATS_AVAILABLE()
elif opt==5:
   TRAIN_ENQUIRY()
elif opt==6:
   CANCEL_TRAIN()
elif opt==7:
   DELAY_IN_ARRIVAL()
elif opt==8:
   PASSENGERS_DETAILS()
elif opt==9:
   ADD_NEW_PASSENGER_DETAILS()
elif opt==10:        
   TICKET_RESERVATION()
elif opt==11:
   SHOW_STATUS_OF_TICKETS()
elif opt==12:
   AC1_FARE_OF_ALL_TRAINS()
elif opt==13:
   AC2_FARE_OF_ALL_TRAINS()
elif opt==14:
   AC3_FARE_OF_ALL_TRAINS()
elif opt==15:
   SLEEPER_FARE_OF_ALL_TRAINS()


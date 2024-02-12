import calendar
import csv
from datetime import *
from csv import*       






#emfanizei ta events
def eventspr(rows,yy,mm):
    
    
       
        

        count = 0
        
        for row in rows:
            
            rowcheck = row[0]

            
          
          

          #rowD = datetime.datetime.strptime(rowcheck,"%Y-%m-%d")
            rr =datetime.strptime(rowcheck, "%Y-%m-%d")
            
            if rr.month == int(mm)  and rr.year == int(yy):
              count += 1
              
              print(f"{count}. [{row[3]}] -> Date: {row[0]}, Time: {row[1]}, Duration: {row[2]}")


             

           
    
        print()
        if count == 0:
          print("αυτόν τον μήνα δεν υπάρχει καμία εκδήλωση!")

        print() 





def Csvreader():
    file = open('events.csv')
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []


    for row in csvreader:

        if any(row):
          rows.append(row)

   
    file.close()  
    return rows






def delete(file_path,row_num):

    rows=[]
    with open(file_path, 'r') as csvfile:
       csvreader = csv.reader(csvfile)
       for i, row in enumerate(csvreader):
          if i != row_num:
              rows.append(row)

# write the updated rows back to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in rows:
            csvwriter.writerow(row)

def eventfounder(rows,yy,mm):
        
    
    
       
        

        count = 0
        data = []
        
        for row in rows:
            
            rowcheck = row[0]

            
          
          

          #rowD = datetime.datetime.strptime(rowcheck,"%Y-%m-%d")
            rr =datetime.strptime(rowcheck, "%Y-%m-%d")
            
            if rr.month == int(mm)  and rr.year == int(yy):
              count += 1
              data.append(row)
              
              


             

           
    
        

        return data    



def  found_num(file_path,change_row):
        


        # specify the target row
        target_row = change_row

# initialize counter
        count = 0

# read the CSV file
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if row == target_row:
                    count += 1

# print the count
        return count





def every_month(year,month,rows):


 
  days=['ΔΕΥ','ΤΡΙ','ΤΕΤ','ΠΕΜ','ΠΑΡ','ΣΑΒ','ΚΥΡ']
  months=['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΪ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']


 
  cm=month#currentmonth
  cy=year#currentyear

  arr =calendar.monthcalendar(cy,cm)
  c=calendar.monthrange(cy,cm)#diarkeia twrinou mhna
# To len(calendar.monthcalendar(cy,cm)) mas deixnei to plhthos twn evdomadwn toy mhna
#ta position twn hmerwn morfhs k[i][j], to j mas deixnei poses meres den anhkoun ston twrino mhna gia thn prwth evdomada

  pm=cm-1#previous month
  nm=cm+1#next month
  if cm>1 and cm<12:
      p = calendar.monthrange(cy, pm)  # diarkeia previous month
      n = calendar.monthrange(cy, nm)  # diakeia next month
  elif cm==1:
      pm=12
      py=cy-1
      p = calendar.monthrange(py, pm)
      n = calendar.monthrange(cy, nm)
  else:
      nm=1
      ny=cy+1
      p = calendar.monthrange(cy, pm)
      n = calendar.monthrange(cy, nm)
  p=list(p)
  n=list(n)
  k=p[1]-c[0]+1 #oi meres pou anhkoun ston prohgoumeno mhna alla emfanizontai
  for j in range(7):#filling days of previous month
    if j==0:
        if arr[0][0]!=0:#ean o mhnas ksekinaei me thn arxh thw evdomadas
            break
        else:
            arr[0][j]=k
    else:
        if arr[0][j]==0:
            arr[0][j]=k+1
        k=k+1
  a=0#deikths hmerwn kainourgioy mhna
  numweeks=len(calendar.monthcalendar(cy,cm))-1
  for j in range(7):#filling days of the next month
    if arr[numweeks][j]==0:
        arr[numweeks][j]=a+1
        a=a+1
  print("─"*50)  #U+2500,Box Drawings Light Horizontal
  print("",months[cm-1],"  ",cy,'\n')
  print("─"*50) #U+2500,Box Drawings Light Horizontal
  w=0
  wl=len(arr)
  #event=True#ENDIKTIKH METAVLHTH GIA THN YPARKSH GEGONOTOS

  #loukas


  for k in range(7):
      print(" ",days[k],end=" |")
      if k==6:
          print(end="\n")

  
  data = []
  data = eventfounder(rows,year,month)
  p= 0
  for week in arr:#properly showcasing the calendar
      w=w+1
      
     
      for i in week:
           
           
           
           if arr[0]==week:
               if i>10:
                  
                   if eventp(data,cm-1,i,p):
                      p +=1
                     
                     
                      print("  *",i,sep="",end=" |")
                   else:
                      print("  ", i, end=" |")
               else:
                 
                    if eventp(data,cm,i,p):
                        p+=1 
                      
                        

                        print('[ *', i, sep="",end="] |")
                    else:
                        print('[ ',i,end="] |")
           else:
               if arr[wl-1]!=week:
                   if i<10:
                       if eventp(data,cm,i,p):
                           p+=1
                           
                           
                           print('[ *',end='')
                       else:
                           print('[  ',end='')
                   else:
                       if eventp(data,cm,i,p):
                           p+=1
                           
                           print('[*',end='')
                       else:
                           print('[ ',end='')
                   print(i,end='] |')
               else:
                   if i>10:
                       if eventp(data,cm,i,p):
                           p+=1
                           
                           print('[*',i,sep='',end='] |')
                       else:
                           print('[', end=' ')
                           print(i, end='] |')
                   else:
                       if eventp(data,cm+1,i,p):
                           p+=1
                           
                           print("   *", i,sep='', end=" |")
                       else:
                           print("   ",i,end=" |")
      print()
  print('\n',"─"*50) #U+2500,Box Drawings Light Horizontal

def eventp(data,month,day,p):
    
    
         if p < len(data):
            rowcheck = str(data[p][0])

            rr =datetime.strptime(rowcheck, "%Y-%m-%d")

            if month == rr.month and day == rr.day  :
               return True
            else:
               return False


def change_val(file_path,cc,rows):




 while True:  
   new_date = input(f"Ημερομηνία γεγονότος ({rows[cc][0]}):")
   if new_date == "":
       new_date = rows[cc][0]
   else:
       try:
                date_new_obj =datetime.strptime(new_date, "%Y-%m-%d")
                
                 
                if(date_new_obj.year <= 2022):
                    print(f"{new_date} μη έγκυρη ημερουμηνία.")
                    break
                    

                



       except ValueError:
                print(f"{new_date} μη έγκυρη ημερουμηνία.")
                break
                

       print(f"{new_date} έγκυρη ημερουμηνία.")   

   new_time = input(f"Ώρα γεγονότος ({rows[cc][1]}):" ) 
   if new_time == "":
      new_date = rows[cc][1]
   else:
         
        try:
                new_time_obj =datetime.strptime(new_time, "%H:%M:%S")
                
                
                 
                
        except ValueError:
                print(f"{new_time} μη έγκυρη ημερουμηνία.")
                break    



   new_dur = input(f"Διάρκεια γεγονότος ({rows[cc][2]}):")
   if new_dur == "":
       new_dur = rows[cc][2]
            

        
   new_title = input(f"Τίτλος γεγονότος ({rows[cc][3]}):")
   if new_title == "":
      new_title = rows[cc][3]

   dict = {'Date':new_date,'Hour':new_time,'Duration':new_dur,'Title':new_title}
   
   
  

   return dict
   
   



   break









   

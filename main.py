import calendar
import csv
from datetime import *
from def_methods import*
import sys




field_names = ['Date','Hour','Duration','Title']

#shmerinh mera (year , month ) se metablhtes
today_date = date.today()
month = today_date.month
year = today_date.year

#csv events file 
file = open('events.csv')
type(file)
csvreader = csv.reader(file)


#header of wvwry category
header = []
header = next(csvreader)

#rows of events.csv 
rows = []

for row in csvreader:
    rows.append(row)
file.close()


#rowcheck = rows[0][0]
#print(rowcheck)
#rowD = datetime.strptime(rowcheck,"%Y-%m-%d")
#print(rowD.month)










while True:

    
    rows = Csvreader()  
    
    
     

   


    every_month(year,month,rows)

    

    print("""\nΠατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τιςπαρακάτω επιλογές:""")
    print(""""-" για πλοήγηση στον προηγούμενο μήνα""")
    print(""""+" για διαχείριση των γεγονότων του ημερολογίου""")
    print(""""*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα""")
    

    # Get the user's choice
    choice = input("\nPlease enter your choice: ")


    # Navigate to the previous or next month
    if choice == "":
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    elif choice == "-":
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
    elif choice == "+":
        print("+")
        #new menu
        print("\nΔιαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:")
        print("\n1 Καταγραφή νέου γεγονότος")
        print("\n2 Διαγραφή γεγονότος")
        print("\n3 Ενημέρωση γεγονότος")
        print("\n0 Επιστροφή στο κυρίως μενού")
        choice2 = input("\n->")

        if choice2 == "1":
            print("Εισαγωγή νέου γεγονότος")

            
            date_new = input("\nΗμερουμηνία γεγονότος (παράδειγμα:YYYY-MM-DD) : ")
            
            #elegxos hmeroyminias
            try:
                date_new_obj =datetime.strptime(date_new, "%Y-%m-%d")
                
                 
                if(date_new_obj.year <= 2022):
                    print(f"{date_new} μη έγκυρη ημερουμηνία.")
                    continue

                



            except ValueError:
                print(f"{date_new} μη έγκυρη ημερουμηνία.")
                continue

            print(f"{date_new} έγκυρη ημερουμηνία.")
                




            time_new = input("\nΏρα γεγονότος (παράδειγμα: HH:MM:SS) :")
            try:
                time_new_obj =datetime.strptime(time_new, "%H:%M:%S")
                
                
                 
                
            except ValueError:
                print(f"{time_new} μη έγκυρη ημερουμηνία.")
                continue   

            #εισαγωγη διάρκειας
            duration_new = input("\nΔιάρκεια γεγονότος σε λεπτά :")
            #εισαγωγη τιτλου
            title_new = input("\nΤίτλος γεγονότος :")

            dict = {'Date':date_new,'Hour':time_new,'Duration':duration_new,'Title':title_new}

            with open('events.csv','a')as f_obj:
                dictwriter_obj = DictWriter(f_obj,fieldnames=field_names)
                dictwriter_obj.writerow(dict)
                rows = Csvreader()
                f_obj.close()
                









            

        elif choice2 == "2":
            yy = input("Εισάγετε έτος:\n")
            mm = input("Εισάγετε μήνα:\n")
            eventspr(rows,yy,mm)
            data = []

            data = eventfounder(rows,yy,mm)
            
            if data :
                checknumber = input("->")
                if len(data)>=int(checknumber):
                 
            
            
            
                 new_data_row = data[int(checknumber)-1]
                 cc = found_num("events.csv",new_data_row)
                 delete("events.csv",cc)
            

        elif choice2 == "3":
            
            yy = input("Εισάγετε έτος:\n")
            mm = input("Εισάγετε μήνα:\n")
            eventspr(rows,yy,mm)
            data = []

            data = eventfounder(rows,yy,mm)
            
            
            if data :
                checknumber = input("->")
                if len(data)>=int(checknumber):
                 
            
            
            
                 new_data_row = data[int(checknumber)-1]
                 cc = found_num("events.csv",new_data_row)
                 ch_row = change_val("events.csv",cc,rows)
                 delete("events.csv",cc)
                 with open('events.csv','a')as f_obj:
                     dictwriter_obj = DictWriter(f_obj,fieldnames=field_names)
                     dictwriter_obj.writerow(ch_row)
                     rows = Csvreader()
                     f_obj.close()




        elif choice2 == "0":
            continue
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ προσπαθησε ξανα.")
              
    elif choice == "*":
        print("*") 
        yy = input("Εισάγετε έτος:\n")
        mm = input("Εισάγετε μήνα:\n")
        eventspr(rows,yy,mm)#ektipwsi olwn twn events


    elif choice == "q":
        
        sys.exit()
        
    
    else:
        print("Μη έγκυρη επιλογή. Παρακαλώ προσπαθησε ξανα.")



      


    



        


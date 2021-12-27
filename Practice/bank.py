import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
from getpass import getpass
import mysql.connector


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.environ.get('DB_PASS'),
    database = 'bank'
)


def register():
    
    """
    This function for new users who wants to register on bank portal.
    """
    Username = input("Create Username : ")
    Password = getpass("Create Password : ")
    Password1 = getpass("Conform Password : ")
    
    if Password != Password1:
        print("Password don't match, Please Re-enter..")
        register()
        
    else:
        if len(Password) <= 6:
            print("Password too short, Please Re-enter.")
            register()
            
        else:
            mycursor = conn.cursor()
            mycursor.execute("SELECT user_name FROM authentic")
            lst = mycursor.fetchall()
            if (Username,) in lst:
                print('exists')
                register()
            else:
                sql = "INSERT INTO authentic VALUES (%s, %s)"
                val = (Username, Password)
                
                mycursor = conn.cursor()
                mycursor.execute(sql, val)
                
                conn.commit()
                print("Register successfully!")
                Main()


def access():
    """
    This function is used for Customer login.
      - If customer login successfully then he or she can perform all bank operations.
      - NOTE:- Before login it's mandatory to register.
    """
    Username = input("Enter Username : ")
    Password = getpass("Enter Password : ")
        
    mycursor = conn.cursor()
    mycursor.execute("SELECT user_name,password FROM authentic")
    lst = mycursor.fetchall()
    if (Username,Password) in lst:
        print("Login Successful!")
        print("############### WELCOME TO SBI BANK ##################")
        main()
    else:
        print("Not Registered.Please register")
        register()
        

def Main():
    while True:
        print("1) Register \t\t 2) Login \t\t 3) Exit")
        responce = int(input("Enter your responce: "))
        if responce == 1:
            register()
        elif responce == 2:
            access()
        elif responce == 3:
            break
        
               
def generate_account_no():
    
    """
    Auto generated account number using datetime module.
    return account number.
    """
    account_number = datetime.now().strftime("SBI350%Y%m%d%M%S")
    return account_number

def send_mail(email,n,ad,ob,account_number):
    """
    This Function send mail to user automatically when user create new account.
    """
    
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login((os.environ.get("mailuser")),(os.environ.get("mailpass")))
    message = EmailMessage()
    message['Subject'] = 'JD-SBIINB'
    message['From'] = os.environ.get('mailuser')
    message['To'] = email
    message.set_content(f"""
    <html>
    <body>
     Hii {n}, <br> &nbsp;&nbsp;&nbsp;&nbsp; Thank's for creating account in SBI.<br>
     Your account details:- <br>
     &nbsp;&nbsp;Account Number:- {account_number},<br>
     &nbsp;&nbsp;Branch:- {ad}<br>
     &nbsp;&nbsp;Amount:- {ob}<br>
     <br>For more details please visit <a href="https://www.sbi.com">www.sbi.com</a>
    </body>
    """,subtype = 'html')
    connection.send_message(message)
    connection.quit()
    
            

def open_account():
    
    """
    This Function opens new account for customers.
    Return account number.
    
    """
   
    n = input("Enter name :- ")
    db = input("Enter D.O.B :- ")
    ad = input("Enter address :- ")
    ob = int(input("Enter opening balance :- "))
    pn = input("Enter phone number :- ")
    email = input("Enter you email:- ")
    
    account_number = generate_account_no()
    
    data1 = (n, account_number, db, ad, ob, pn)
    data2 = (n, account_number, ob)
    
    sql1 = "insert into account values (%s, %s, %s, %s, %s, %s)"
    sql2 = "insert into amount values (%s, %s, %s)"
    
    mycursor = conn.cursor()
    
    mycursor.execute(sql1, data1)
    mycursor.execute(sql2, data2)
    
    conn.commit()
    
    send_mail(email,n,ad,ob,account_number)
   
    
    print(f"Data entered Successfully.\n YOUR ACCOUNT NUMBER IS:-{account_number} ")
    
    
def deposite_amount():
    
    """
    This function deposite amount to customers account.
    Return available balance
    """
    
    am = int(input("Enter amount :- "))
    ac = input("Enter account number :- ")
    
    sql = "select balance from amount where acno = %s"
    data = (ac,)
    mycursor = conn.cursor()
    mycursor.execute(sql, data)
    myresult = mycursor.fetchone()
    total_amount = myresult[0] + am
    
    sql1 = "update amount set balance = %s where acno = %s"
    val1 = (total_amount, ac)
    
    mycursor.execute(sql1, val1)
    
    conn.commit()
    
    print(f"Amount Deposite Successfully.\n Available balance:-{total_amount}")
    
    
def withdraw_amount():
    
    """
    This Function withdraw amount from customers account.
    Return available balance.
    """
    am = int(input("Enter amount :- "))
    ac = input("Enter account number :- ")
    
    sql = "select balance from amount where acno = %s"
    data = (ac,)
    mycursor = conn.cursor()
    mycursor.execute(sql, data)
    myresult = mycursor.fetchone()
    total_amount = myresult[0] - am
    
    sql1 = "update amount set balance = %s where acno = %s"
    val1 = (total_amount, ac)
    
    mycursor.execute(sql1, val1)
    
    conn.commit()
    
    print(f"Amount withdraw Successfully.\n Available balance:-{total_amount}")
    
        
def balance():
    
    """
    This function shows balance from customers account.
    Return available balance.
    """
    ac = input("Enter account number :- ")
    sql = "select balance from amount where acno = %s"
    val = (ac,)
    
    mycursor = conn.cursor()
    
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    
    print(f"Balance for account: {ac} is {myresult[0]}")
    
    
def display_account_details():
    
    """
    This function display all details of customers.
    Return list of data
    """
    
    ac = input("Enter account number :- ")
    sql4 = "select * from account where acno = %s"
    val4 = (ac,)
    
    mycursor = conn.cursor()
    
    mycursor.execute(sql4, val4)
    
    print(f"Your Account Details is \n{mycursor.fetchall()}")
       
    
def close_account():
    
    """
    This function is used when customer want to delete account.
    """
    
    ac = input("Enter account number :- ")
    sql1 = "delete from account where acno = %s"
    sql2 = "delete from amount where acno = %s"
    val = (ac,)
    
    mycursor = conn.cursor()
    
    mycursor.execute(sql1, val)
    mycursor.execute(sql2, val)
    
    conn.commit()
    
    print("Account closed successfully.")
    
    
def main(): 
    
    """
    This is main function.
    User can choose verious options given in this function.
    """
    
    while True:
    
        print("""
        1. OPEN NEW ACCOUNT
        2. DEPOSITE AMOUNT
        3. WITHDRAW AMOUNT
        4. BALANCE ENQUIRY
        5. DISPLAY ACCOUNT DETAILS
        6. CLOSE ACCOUNT
        7. EXIT
        
        """)
        choice = int(input("############### WELCOME TO SBI ################## \n Enter Task Number :- "))
        if choice == 1:
            open_account()
         
        elif choice == 2:
            deposite_amount()
        
        elif choice == 3:
            withdraw_amount()
        
        elif choice == 4:
            balance()
    
        elif choice == 5:
            display_account_details()
        
        elif choice == 6:
            close_account()
           
        elif choice == 7:
            print("############# THANK'S FOR VISITING SBI BANK. #################")
            break
        
        else:
            print("Wrong choice\n Please Enter from below choices: ")
            
Main()
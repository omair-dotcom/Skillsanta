database={
       'eddygrant000':{
           'name':'Sachin',
           'age':22,
           'email':'eddygrant000@gmail.com',
           'password':1234,
           'amount':20000,
           },
       'omair123':{
           'name':'Omair',
           'age':22,
           'email':'omair9.ok@gmail.com',
           'password':2098,
           'amount':50000,
           }
    }
def banking():
    ch1=0
    while ch1!=4:
        print('Enter your choice:')
        print('1.Check Balance\n2.Deposit Balance\n3.Withdrawl Balance\n4.Logout')
        ch1=int(input())
        if ch1==1:
            print('Current Balance:',database[user]['amount'])
        if ch1==2:
            add=int(input('Enter amount to be deposited:'))
            database[user]['amount']+=add
            print('Current Balance:',database[user]['amount'])
        if ch1==3:
            sub=int(input('Enter amount:'))
            print('Collect your cash',sub)
            database[user]['amount']-=sub
            print('Current Balance',database[user]['amount'])
def newpass():
    email=input('Enter your email address:')
    if email==database[user]['email']:
        new=int(input('Enter new password(4 digit code):'))
        database[user]['password']=new
        print('Your new password is set')
    else:
        print('Invalid email address')
def authenticate():
    global user
    user=input('Enter username:')
    passrd=int(input('Enter password(4-digit code):'))
    if user in database.keys():
        if passrd==database[user]['password']:
            print('Login success\nWelcome ',database[user]['name'])
            banking()
        else:
            print('Password failed')
            print('Forgot password... Do you want to change your password?(yes/no)')
            chgpass=input()
            if chgpass=='yes':
                newpass()
    else:
        print('Account does not exist')
ch=0
while ch!=3:
    print('Enter your choice:')
    print('1.Sign in\n2.Sign up\n3.Exit')
    ch=int(input())
    if ch==1:
        authenticate()
    if ch==2:
        dic={}
        newuser=input('Enter new username:')
        newname=input('Enter name:')
        age=int(input('Enter your age:'))
        newemail=input('Enter your email address:')
        newpass=int(input('Enter password:'))
        amount=int(input('Enter the amount:'))
        dic={newuser:{
            'name':newname,
            'age':age,
            'email':newemail,
            'password':newpass,
            'amount':amount,
            }}
        database.update(dic)
        print('Username successfully created ')

        

 

     

import getpass
options=('1. DEPOSIT',
         '2. WITHDRAW',
         '3. CHECK BALANCE')
pwd=True
balance=0
running=True



    
while pwd:
    print('------------WELCOME TO ATMP BANK-----------')
    print('Enter name and password')
    print('---')
    name=input("Enter Name(q to quit): ")
    if name.lower()=='q':
        pwd=False
    else:
        password=getpass.getpass(prompt='Enter your 4 digit pin: ').strip()

        if password.isdigit() and len(password)==4:
            print('Successfully logged in!')
            while running:
                
                print('------')
                print(f'ACCOUNT NAME: {name}')
                print('Please Select an option')
                for option in options:
                    print(option)
                choice=input('YOUR SELECTION: ')
                if choice=="1":
                    while True:
                        print('----DEPOSIT-----')
                        deposit_amount=input('Enter Amount:')
                        if deposit_amount.isdigit():
                            balance+=int(deposit_amount)
                            print(f'${deposit_amount} succefully deposited')
                            break
                        else:
                            print('Enter a valid amount')

                elif choice=="2":
                    while True:
                        print('-------WITHDRAW------------')
                        print(f'BALANCE: ${balance}')
                        withdraw_amount=input('WITHDRAW AMOUNT: ')
                        if withdraw_amount.isdigit() and int(withdraw_amount)<=balance:
                            pass_withdraw=getpass.getpass('ENTER PIN:')
                            if int(pass_withdraw)==password:
                                balance-=int(withdraw_amount)
                                print(f'You have succesfully withdrawn: ${withdraw_amount}')
                                break
                            else:
                                print('Wrong PIN')
                                break
                        elif withdraw_amount.isdigit() and int(withdraw_amount)>balance:
                            print('Your Balance is insufficient.')
                            break
                        else:
                            print('Invalid amount')
                            break
                elif choice=='3':
                    print('----------YOUR BALANCE----------')
                    print("*"*len(str(balance))
                    check_balance_password=getpass.getpass(prompt='ENTER PIN: ')
                    if int(check_balance_password)==password:
                        print(f'BALANCE: ${balance}')
                        break
                    else:
                        print('Wrong PIN')
                elif choice=='q':
                    running=False

        else:
            print('Enter a valid 4 digit pin')




#UNCOMPLETE
        
 




           
    
def menu():
    print('*'*20)  
    print('*** Welcome to my system ***')  
    print('Choose from the following options:')
    print('1. Register') 
    print('2. Log in') 
    print('3. Exit!') 
    print('*'* 30)
    
    
def main():
    while True:
        print('*** Welcome to my system ***')  
    print('Choose from the following options:')
    print('1. Register') 
    print('2. Log in') 
    print('3. Exit!')
    
    choice = input('>')
        
    if choice == '1':
            register_user()
            print('User registered!!')
    elif choice == '2':
            if log_in_user():
                print('You are logged in !!!!!')
            else:
                print('Incorrect log in')
    elif choice == '3':
            print('Good bye!!')
    break                 
    
    
      

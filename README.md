# Login-Form-Brute-Force-Py

## This is a Login form Brute Forcer using a Python Script.

***The script Enumerates through specific number of usernames and a list of potential passwords***


Some Requirements:
```
1) Website | Webserver 
2) List of passwords
```

#
***Code Execution Flow***

**The Code simply takes each username and iterates over all of the passwords from the list, if correct password found it printes the user and passsword then continues to search till finishing the whole names list**
#


**Don't forget to install the requests module `pip install requests`.**


### Needle:
 - The needle is used here to specify whether the reuqest succeeded for the credentials or not, but how??
 - On the script there is a conditional statement to check, if there is at least one character from the needle found on the response then the request has succeeded.
 - Note that we are assuming to know what's inside the Welcome page, or whatever after logging in
 - Another mechanism to use the error code to check if the request


![image](https://github.com/AwsGhanem/Login-Form-Brute-Force-Py/assets/123994471/0f3f1ea1-12e1-43fb-8d91-20ef765ebf12)

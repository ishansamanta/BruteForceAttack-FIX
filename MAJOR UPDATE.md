# MAJOR UPDATE !!! ON Weak file :
## Security patch update:  
### 1. Added encoder/ basic algorithm, for encrypting stored user data in user_encrypted.txt file.. it stores the password
### 2. Added a cooldown after 3 attempts to slow down fast brute force attack using time module  (time.sleep(2))// for i in range(10, 0 ,-1) This make 10 seconds cooldown more longer due to time.sleep(2)
### 3 Overall performance improved
### 4. Logical error fixed 
### Feedback : No runtime error detected yet

# GUIDELINES FOR USERS: 
## THE ALGORITHM IS BASIC AND CAN BE CRACKED OR REVERSED WITH THE HELP OF DECODER SYSTEM WHICH I WILL BE ADDING ON DIFFERENT PYTHON FILE. IT IS PURELY ON LOGIC BASED SECURITY ALGORITHM NO ADVANCE LIBRARY IS USED
### IF U WANT TO CHANGE THE TESTING PASSWORD KINDLY CHANGE IT IN THE OBJECT SECTION AND ALSO USE THE ENCODER TO ENCODE IT AND UPDATE THE TXT FILE FOR FAVOURABLE OUTCOME OF THE CODE.
### GOAL WAS THAT IF ANYBODY ENTERS OR GETS ACCESS TO THE USER DATA TXT FILE,, HE OR SHE CANNOT UNDERSTAND THE PASSWORD AS IT WILL BE STORED THERE IN ENCRYPTED FORMAT AND ONLY THE SECURED PYTHON FILE CAN READ IT

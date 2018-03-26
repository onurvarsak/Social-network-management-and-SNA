# -*- coding: utf-8 -*-


#######################################################################################################################
######################################################### InsertionSort ###############################################
#######################################################################################################################
def InsertionSort(alist):
    #-------------------------------------------
    for i in range(1,len(alist[1])):
        value = alist[1][i]
        value_str = alist[0][i]
        position = i
        #-------------------------------------------
        while position > 0 and alist[1][position-1] > value:
            #-------------------------------------------
            alist[1][position] = alist[1][position-1]
            alist[0][position] = alist[0][position-1]            
            alist[1][position-1] = value
            alist[0][position-1] = value_str            
            position = position-1
        #-------------------------------------------    
        alist[1][position] = value
        alist[0][position] = value_str
        

########################################################################################################################
########################################################## Add User ####################################################
########################################################################################################################
def au(newuser, existinguser):
    #-------------------------------------------
    mylist[0].append(newuser)
    mylist.append([])
    #-------------------------------------------
    mylist[mylist[0].index(existinguser)+1].append(newuser)
    mylist[mylist[0].index(newuser)+1].append(existinguser)
    #-------------------------------------------
    print "User \'"+newuser +"\' has been added and tied to \'"+existinguser+"\' successfully"
    
########################################################################################################################
######################################################## Remove user ###################################################
########################################################################################################################  
def ru(username):
    #-------------------------------------------
    a = mylist[0].index(username)
    del mylist[0][a]
    del mylist[a+1]
    #-------------------------------------------
    for i in range(len(mylist)):
        x = 0
        for j in range(len(mylist[i])):
            if mylist[i][j-x] == username:
                del mylist[i][j-x]
                x += 1
    #-------------------------------------------
    x = 0
    for i in range(len(mylist)):
        if mylist[i-x] == []:
            del mylist[i-x]
            del mylist[0][i-x-1]    
            x += 1
    #-------------------------------------------            
    print "User \'"+ username +"\' and its all relations have been removed successfully."
    
    
    
    
###########################################################################################################################    
########################################################## Add New Relation ###############################################
###########################################################################################################################
def ar(sourceuser, targetuser):
    #----------------------------------------------------------------------------------------------
    mylist[mylist[0].index(sourceuser)+1].append(targetuser)
    mylist[mylist[0].index(targetuser)+1].append(sourceuser)
    #------------------------------------------------------------------------------------------------------
    print "Relation between \'"+sourceuser+"\' and \'"+targetuser+"\' has been added succesfully."
    
    
    
    
############################################################################################################################
########################################################## Remove Existing Relation ########################################
############################################################################################################################    
def rr(sourceuser, targetuser):
    #-------------------------------------------
    x=0
    mylist[mylist[0].index(sourceuser)+1].remove(option[2])
    mylist[mylist[0].index(targetuser)+1].remove(option[1])
    #-------------------------------------------
    for i in range(len(mylist)):
        #-------------------------------------------
        if mylist[i-x] == []:
            #-------------------------------------------
            del mylist[i-x]
            del mylist[0][i-1-x]
            x+=1
    #-------------------------------------------
    print "A relation between \'",sourceuser,"\' and \'",targetuser,"\' has been removed successfully."




###########################################################################################################################
########################################################## Rank users #####################################################
###########################################################################################################################
def pa(toplistsize):
    #-------------------------------------------
    mylist_sort=[[],[]]
    
    #-------------------------------------------
    for i in range(len(mylist[0])):
        print "User \'"+ mylist[0][i] +"\' has ", len(mylist[i+1]) ," friends"
        
    #-------------------------------------------
    for i in range(len(mylist[0])):
        mylist_sort[0].append(mylist[0][i])
        mylist_sort[1].append(len(mylist[i+1]))
        
    #-------------------------------------------
    InsertionSort(mylist_sort)
    for i in range(toplistsize):
        print str(i+1)+". \'"+mylist_sort[0][-1-i]+ "\':",mylist_sort[1][-1-i]





###########################################################################################################################
#################################################### Suggest friendship: ##################################################
########################################################################################################################### 
def sa(username, md):
    alist=[]
    blist =[[],[]]
    clist=  [[],[]]
    x = 0                                   
    a = mylist[0].index(username)
    #-------------------------------------------
    for j in mylist[a+1]:
        alist.append(j)
    #-------------------------------------------
    for j in alist: 
        a=mylist[0].index(j)
        #-------------------------------------------
        for k in mylist[a+1]:
            b = mylist[0].index(username) 
            #-------------------------------------------
            for l in mylist[b+1]:     
                if l != k: 
                    x+=1
                    if x == len(mylist[b+1]):
                        if k != username:
                            blist[0].append(k)
                            blist[1].append(1)
                        x=0

    #-------------------------------------------       
    for i in range(len(blist[0])):
        blist[1][i]= blist[0].count(blist[0][i])
        
    #-------------------------------------------
    x= 0
    for i in range(len(blist[0])):
        x=0
        #-------------------------------------------
        for j in range(i,len(blist[0])):
            #-------------------------------------------
            if blist[0][i] == blist[0][j]:
                x+=1
             #-------------------------------------------   
            if j == len(blist[0])-1:
                if x == 1:
                    clist[0].append(blist[0][i])
                    clist[1].append(blist[1][i])
                    x=0
                    
    #-------------------------------------------
    InsertionSort(clist)
    print "Suggestion List for \'",username,"\' (when MD is ",str(md),"):"
    #-------------------------------------------
    for i in range(len(clist[1])):
        if clist[1][-1-i] >= md :
            print username,"  has ",str(clist[1][-1]-i)," mutual friends with ",clist[0][-1-i]
    



######################################################## FILE OPENING #####################################################
import inspect;
import os;
commandsP1 = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ "commandsP1.txt", "r") 
sn = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ "sn.txt", "r") 

######################################################## CHANGEABLES ######################################################
my_input = []
mylist  = []
mylist2 = []
mylist3 = []
mylist4 = [[]]
mylist5 = []
alist=[]
blist =[[],[]]
clist=  [[],[]]

#-------------------------------------------
for i in commandsP1:
    my_input.append(i.split())

#-------------------------------------------
for i in sn:
    mylist.append(i.split("\n"))

#-------------------------------------------
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        if mylist[i][j] != '':
            mylist2.append(mylist[i][j])

#-------------------------------------------
mylist = []
for i in mylist2:
    mylist3.append(i.split(":"))


#-------------------------------------------
for i in range (len(mylist3)):
    mylist4.append([])
    mylist4[0].append(mylist3[i][0])
    mylist4[mylist4[0].index(mylist3[i][0])+1].append(mylist3[i][1])

#-------------------------------------------
mylist5.append(mylist4[0])
for i in range(1,len(mylist4)):
    for j in range(len(mylist4[i])):
        mylist5.append(mylist4[i][j].split(" "))

######################################################## FILE CLOSING #####################################################
commandsP1.close()
sn.close()

#----------------------------------------------------
mylist = mylist5

###########################################################################################################################
###########################################################################################################################
#################################################### MAIN PROGRAM #########################################################
###########################################################################################################################
########################################################################################################################### 

for option in my_input:
    str(option).split()
    
########################################################## Add User ####################################################
    if option[0] == "AU":
        #-------------------------------------------
        sayac = 1
        if len(option) != 3:
            print "Error: Wrong input type for 'AU'!"
        else:
            #-------------------------------------------
            for i in range(len(mylist[0])):
                if sayac == 1:
                    #-------------------------------------------
                    if option[1] == mylist[0][i]:
                        print "This user already exists!!"
                        sayac = 0
                        break
                    else:
                        if mylist[0][i] == mylist[0][-1]:
                            for j in range(len(mylist[0])):
                                if sayac == 1:
                                    #-------------------------------------------
                                    if option[2] == mylist[0][j]:
                                        au(option[1], option[2])
                                        sayac = 0
                                    else:
                                        if mylist[0][j] == mylist[0][-1]:
                                            print "There is no user named \'"+option[2]+"\'"
                                            sayac = 0
                                            break
########################################################## Remove user ####################################################  
    elif option[0] == "RU":
        #-------------------------------------------
        x = 0
        if len(option) != 2:
            print "Error: Wrong input type! for 'RU'!"
        else:
            #-------------------------------------------
            for i in mylist[0]:
                #-------------------------------------------
                if option[1] == i:
                    ru(option[1])
                    break
                #-------------------------------------------
                else:
                    x += 1
                    if x == len(mylist[0]):
                        print "There is no user named \'"+ option[1] +"\'!!"
                        
########################################################## Add New Relation ###############################################
    elif option[0] == "AR":
        #-------------------------------------------
        x = 0
        y = 0
        z = 0
        sayac = 1
        
        if len(option) != 3:
            print "Error: Wrong input type! for 'AR'!"
        else:
            #-------------------------------------------
            for i in mylist[0]:
                
                if sayac == 1:
                    
                    if i == option[1]:
                        #-------------------------------------------
                        for j in mylist[0]:
                            #-------------------------------------------
                            if sayac == 1:
                               
                                if j == option[2]:
                                    a = mylist[0].index(option[1])
                                    for k in mylist[a+1]:
                                        if sayac == 1:
                                            #-------------------------------------------
                                            if option[2] == k:
                                                print "A relation between \'"+option[1]+"\' and \'"+option[2]+"\' already exists!!"
                                            #-------------------------------------------
                                            else:
                                                x += 1
                                                if x == len(mylist[a+1]):
                                                    ar(option[1], option[2])
                                                    sayac == 0
                                                    break
                                #-------------------------------------------
                                else:
                                    y += 1
                                    if y == len(mylist[0]):
                                        print "No user named \'"+option[1]+"\' or \'"+option[2]+"\' found!!"+option[2]
                                        sayac == 0
                                        y=0
                                        break
                    #-------------------------------------------
                    else:
                        z += 1
                        if z == len(mylist[0]):
                            print "No user named \'"+option[1]+"\' or \'"+option[2]+"\' found!!"+ option[1]
                            sayac == 0
                            z=0
                            break

                        
########################################################## Remove Existing Relation ########################################
    elif option[0] == "RR":
        #-------------------------------------------
        x = 0
        y = 0
        z = 0
        sayac = 1
        #-------------------------------------------
        if len(option) != 3:
            print "Error: Wrong input type! for 'RR'!"
        else:
            for i in range(len(mylist[0])):
                if sayac == 1:
                    if option[1] == mylist[0][i]:
                        for j in range(len(mylist[0])):
                            if sayac == 1:
                                if option[2] == mylist[0][j]:
                                    a = mylist[0].index(option[1])
                                    for k in range(len(mylist[a+1])):
                                        if sayac == 1:
                                            #-------------------------------------------
                                            if mylist[a+1][k] == option[2]:
                                                rr(option[1], option[2])
                                                sayac = 0
                                                break
                                            #-------------------------------------------
                                            else:
                                                x += 1
                                                if x == len(mylist[a+1]):
                                                    print "No relation between \'"+option[1]+"\' and \'"+option[2]+"\' found!!"
                                                    sayac = 0 
                                                    break
                                #-------------------------------------------
                                else:
                                    y += 1
                                    if y== len(mylist[0]):
                                        print "No user named \'"+option[1]+"\' or \'"+option[2]+"\' found!!"
                                        sayac = 0
                                        break 
                    #-------------------------------------------
                    else:
                        z += 1
                        if z == len(mylist[0]):
                            print "No user named \'"+option[1]+"\' or \'"+option[2]+"\' found!!"
                            sayac = 0
                            break
                      
########################################################## Rank users #####################################################        
    elif option[0] == "PA":
        #-------------------------------------------
        if len(option) != 2:
            print "Error: Wrong input type! for \'"+ option[0] +"\'!"
        else:
            if int(option[1]) > len(mylist[0]):
                print "Invalid input since n is greater than ",len(mylist[0])            
            else:
                pa(int(option[1]))
                
    
##################################################### Suggest friendship ##################################################         
    elif option[0] == "SA":
        #-------------------------------------------
        x=0
        if len(option) != 3:
            print "Error: Wrong input type! for \'"+ option[0] +"\'!"
        else: 
                for i in mylist[0]:
                    #-------------------------------------------
                    if option[1] == i:
                        if int(option[2]) > len(mylist[mylist[0].index(option[1])+1]):
                            print "User \'"+option[1]+"\' has less friend than "+option[2]
                        else:
                           sa(option[1],int(option[2]))
                                
                    #-------------------------------------------    
                    else:
                        x+=1
                        if x== len(mylist[0]):
                            print "No user named \'"+option[1]+"\' found!!"
                
        
########################################################## Else ###########################################################
    else:
        print "Error: Undefined command type!"
 
        
########################################################## FILE WRITTING ##################################################       
new = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ "sn.txt", "w") 
for i in range(len(mylist[0])):
    #-------------------------------------------
    a=""
    a+= mylist[0][i]
    a+=":"
    for j in range( len(mylist[i+1])):
        a+=mylist[i+1][j]
        if j !=len(mylist[i+1])-1:
            a+=" "
    #-------------------------------------------
    if i != len(mylist[0])-1:
        a+="\n"
    new.write(a)
new.close()
       
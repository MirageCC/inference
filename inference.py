
def check1(num1,num2):
    if num1 == num2:
        return 1
    else:
        return 0
def check2(num1,num2,num3):
    if num1 == num2 and num2==num3:
        return 1
    else:
        return 0

def check3(num1,num2):
    if abs(num1-num2)==2:
        return 1
    else:
        return 0

def question1(answer):
    return True

def question2(answer):
    if answer[1] ==0 and answer[4] ==2:
        return True
    elif answer[1] ==1 and answer[4] ==3:
        return True
    elif answer[1] ==2 and answer[4] ==0:
        return True
    elif answer[1] ==3 and answer[4] ==1:
        return True
    return False
def question3(answer):
    temp = []
    temp.append(answer[2])
    temp.append(answer[5])
    temp.append(answer[1])
    temp.append(answer[3])
    tt = set(temp)
    if len(tt)!=2:
        return False
    else:
        if answer.count(temp[0])==2 or answer.count(temp[1])==2:
            return False
    if answer[2] ==0:
        return check2(answer[5],answer[1],answer[3])
    elif answer[2] ==1:
        return check2(answer[2],answer[1],answer[3])
    elif answer[2] ==2:
        return check2(answer[2],answer[5],answer[3])    
    elif answer[2] ==3:
        return check2(answer[2],answer[5],answer[1])

    return False

def question4(answer):
    temp = []
    temp.append(check1(answer[0],answer[4]))
    temp.append(check1(answer[1],answer[6]))
    temp.append(check1(answer[0],answer[8]))
    temp.append(check1(answer[5],answer[9]))
    if temp.count(1) != 1:
        return False
    if answer[3] ==0:
        return check1(answer[0],answer[4])
    elif answer[3] ==1:
        return check1(answer[1],answer[6])
    elif answer[3] ==2:
        return check1(answer[0],answer[8])   
    elif answer[3] ==3:
        return check1(answer[5],answer[9])

    return False    

def question5(answer):
    temp = []
    temp.append(check1(answer[4],answer[7]))
    temp.append(check1(answer[4],answer[3]))
    temp.append(check1(answer[4],answer[8]))
    temp.append(check1(answer[4],answer[6]))
    if temp.count(1) != 1:
        return False
    if answer[4] ==0:
        return check1(answer[4],answer[7])
    elif answer[4] ==1:
        return check1(answer[4],answer[3])
    elif answer[4] ==2:
        return check1(answer[4],answer[8])   
    elif answer[4] ==3:
        return check1(answer[4],answer[6])

    return False    

    
def question6(answer):
    temp = []
    temp.append(check2(answer[7],answer[1],answer[3]))
    temp.append(check2(answer[7],answer[0],answer[5]))
    temp.append(check2(answer[7],answer[2],answer[9]))
    temp.append(check2(answer[7],answer[4],answer[8]))
    if temp.count(1) != 1:
        return False

    if answer[5] ==0:
        return check2(answer[7],answer[1],answer[3])
    elif answer[5] ==1:
        return check2(answer[7],answer[0],answer[5])
    elif answer[5] ==2:
        return check2(answer[7],answer[2],answer[9])    
    elif answer[5] ==3:
        return check2(answer[7],answer[4],answer[8])

    return False


def question7(answer):

    if answer.count(2) <answer.count(1) and answer.count(2) <answer.count(0) and\
       answer.count(2) <answer.count(3) and answer[6]==0 :
       return True
    if  answer.count(1) <answer.count(2) and answer.count(1) <answer.count(0) and\
       answer.count(1) <answer.count(3) and answer[6]==1 :
       return True
    if answer.count(0) <answer.count(3) and answer.count(0) <answer.count(2) and\
       answer.count(0) <answer.count(1) and answer[6]==2 :
       return True
    if answer.count(3) <answer.count(0) and answer.count(3) <answer.count(1) and\
       answer.count(3) <answer.count(2) and answer[6]==3 :
       return True
    return False

def question8(answer):
    temp = []
    key = [6,4,1,9]
    temp.append(check3(answer[0],answer[6]))
    temp.append(check3(answer[0],answer[4]))
    temp.append(check3(answer[0],answer[1]))
    temp.append(check3(answer[0],answer[9]))
   
    if temp.count(1) != 1:
        return False
    if answer[7] ==0:
         return check3(answer[0],answer[6])
    elif answer[7] ==1:
         return check3(answer[0],answer[4])
    elif answer[7] ==2:
         return check3(answer[0],answer[1])
    elif answer[7] ==3:
         return check3(answer[0],answer[9])

    return False

def question9(answer):
    if answer[0]==answer[5]:
        if answer[4]!=answer[5] and answer[8]==0:
            return True
        if answer[4]!=answer[9] and answer[8]==1:
            return True
        if answer[4]!=answer[1] and answer[8]==2:
            return True
        if answer[4]!=answer[8] and answer[8]==3:
            return True
    else:
     
        if answer[4]==answer[5] and answer[8]==0:
            return True
        if answer[4]==answer[9] and answer[8]==1:
            return True
        if answer[4]==answer[1] and answer[8]==2:
            return True
        if answer[4]==answer[8] and answer[8]==3:
            return True

    return False

def question10(answer):
    c = []
    for i in range(4):
        c.append(answer.count(i))
    sc = sorted(c)
    if sc[-1]-sc[0]==3 and answer[9]==0:
        return True
    if sc[-1]-sc[0]==2 and answer[9]==1:
        return True
    if sc[-1]-sc[0]==4 and answer[9]==2:
        return True
    if sc[-1]-sc[0]==1 and answer[9]==3:
        return True
    return False
    
def confirm(answers):
    if question1(answers) and question2(answers) and question3(answers) and\
       question4(answers) and question5(answers) and question6(answers) and \
       question7(answers) and question8(answers) and question9(answers) and \
       question10(answers) :
        return True

    else:
        return False
class getoutofloop(Exception): pass

ch = ['A','B','C','D']
def loop(A,cur=0):
    
    if cur == len(A):
        if confirm(A):
            answer = "正确答案:"
            for i in range(10):
                answer +=ch[A[i]]
                if i<9:
                    answer+=","
            print(answer)  
        return
        
    for col in range(10):
        A[cur],flag = col,True
           
        if  A[col]>3:              
            flag = False
            break
        if flag:
            loop(A,cur+1)

if __name__=="__main__":
    answers = [0]*10
    loop(answers)










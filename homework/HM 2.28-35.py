# excercise 2.28:
# how does Python know to which if and else belongs?
# when we are writing a program 





#exercise 2.29

def answer(result):
    if result == 100:
        return 1
    else:
        return 2

print answer(100)

#exercise 2.30(1)

def gradepoint(score):
    if score >= 90:
        return 4
    else:
        if score >= 80:
            return 3
        else:
            if score >= 70:
                return 2
            else:
                if score >= 60:
                    return 1
                else:
                    return 0

print gradepoint(65)
# this function looks so ugly............rewrite it as
# exercise 2.30(2)
def gradepoint2(score):
    if score >= 90:
        return 4
    if score >= 80:
        return 3
    if score >= 70:
        return 2
    if score >= 60:
        return 1
    return 0

print gradepoint2(59)  #looks better

#excercise 2.31
def gradepoint3(score):
    if score >= 90:
        return 4
    elif score >= 80:
        return 3
    elif score >= 70:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0

print gradepoint3(71)


# exercise 2.33

def Cost(pounds):
    if pounds > 100:
        cost = 100*0.32 + 1.5
        return cost
    else:
        cost = 100*0.32 + 7.5
        return cost

print Cost(120)

# excercise 2.34

def Max(a,b,c):

    if a>b and b>c:
        return a
    if b>a and a>c:
        return b
    if c>b and b>a:
        return c
    return a   # if three numbers are the same:return the first one
print max(102,104,108)

# excercise 2.35

def Pay(payrate,hours):
    if hours > 40:
        pay = hours*1.5*payrate
        return pay
    else:
        pay = hours*payrate
        return pay

print Pay(2,41)
    

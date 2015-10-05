
#SEED            Monday Homework











# excercise 2.28:


# we use indentation to let python know which statemnt belongs to which
# for example: 
#  if x<b:
#     print "hi"
#  else:
#     print "yo"
#in this case, if statment belongs to the thing go directly after : < x<b >, which is a condition statement
#if x<b is true then python will execute the argument intdented directly after if statment before else statemnt
#so if also belongs to them

#else statement will be excuted by python only when x<b is false
#and else statment belongs to the thing indented directly after it
     





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

    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    return c
     # if three numbers are the same:return the first one
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

# exam mark analyser
# Requirements
# user input for mark 100 - 0
mark = int(input("enter the exam mark: "))
# if user mark is greater than 90 and less than 100 print 'excellent' 
if mark >= 90 and mark < 100:
    print("Excellent")
elif mark >=80 and mark<90:
    print("Very Good")
elif mark >= 70 and mark < 80:
    print("Good")
elif mark >= 60 and mark < 70:
    print("better")
elif mark >= 50 and mark < 60:
    print("fair")
elif mark >= 40 and mark < 50:
    print("pass")
else:
    print("failed")    
# if user mark is greater than 80 and less than 90 print 'very good'
# if user mark is greater than 70 and less than 80 print 'good'
# if user mark is greater than 60 and less than 70 print 'better'
# if user mark is greater than 50 and less than 60 print 'fair'
# if user mark is greater than 40 and less than 50 print 'pass'
# if user mark is less than 40 print 'fail'



# HR_Management
import mysql.connector  # type: ignore
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hr_management"
)
mycursor = db.cursor()
print("Welcome !! Human Resource Management System ")
print("1.Add employee\n2.Mark Attendance\n3. Record Salary Payment\n4.Apply for Leave\n5. View Employee Details\n6. View Attendance Report\n7.View Salary Report\n8.View Leave Requests\n9.Manage Leave Requests")
choose = input("Choose one option:")
if choose == '1':
    def Add_Employee():
        print("Add employee")
        s = input("Enter your Employee_id:")
        a = input("Enter your Name:")
        b = input("Enter your Designation:")
        c = input("Enter your join_date:")
        d = input("Enter your salary:")
        sql = "Insert into employee( Employee_id,Name,Designation,join_date,salary) value(%s,%s,%s,%s,%s)"
        val = (s,a,b,c,d)
        mycursor.execute(sql,val)
        db.commit()
        print("New employee added successfully")
    Add_Employee()

elif choose == '2':
    print("Mark Attendance")
    s = input("Enter Employee_id:")
    try:
        sql = "Select Name from employee where Employee_id=%s"
        val = (s,)
        mycursor.execute(sql,val)
        res = mycursor.fetchone()
        for x in res:
            print(x)
        r = input("Enter date:(yyyy-mm-dd)")
        f = input("Enter Attendance_status(Present, Absent, or Leave)")
        sql = "Insert into attendance_report(Employee_id,Name,date,Attendance_status) value(%s,%s,%s,%s)"
        val = (s,x,r,f)
        mycursor.execute(sql,val)
        db.commit()
        print("Attendance mark successfully")
    except Exception:
        print("Employee id not found ! Enter Correct Employee id")

elif choose == '3':
    print("Record Salary Payment")
    a = input("Enter Employee_id:")
    sql = "Select Name from employee where Employee_id = %s"
    val = (a,)
    mycursor.execute(sql,val)
    res = mycursor.fetchone()
    if res:
     for d in res:
        print(d)
    else:
        print("Enter Wrong employee id")
        exit()
    b = input("Enter Payment_date:(yyyy-mm-dd)")
    c = input("Enter Amount_Paid:")
    sql = "Insert into salary_payment(Employee_id,Name,Payment_date,Amount_Paid) value(%s,%s,%s,%s)"
    val = (a,d,b,c)
    mycursor.execute(sql,val)
    db.commit()
    print("Salary payment recorded successfully")

elif choose == '4':
    print("Apply for leave")
    e = input("Enter Employee_id:")
    sql = "Select Name from employee where Employee_id = %s"
    val = (e,)
    mycursor.execute(sql,val)
    res = mycursor.fetchone()
    if res:
     for n in res:
        print(n)
    else:
        print("Enter wrong employee id")
        exit()
    d = input("Enter Leave_date:")  
    r = input("Enter your reason for leave:") 
    s = input("Enter Leave Status:(Pending, Approved, or Rejected)")
    sql = "Insert into Leave_requests(Employee_id,Name,Leave_date,Reason_leave,Status) value(%s,%s,%s,%s,%s)"
    val = (e,n,d,r,s)
    mycursor.execute(sql,val)
    db.commit()
    print("Leave request submitted successfully")

elif choose == '5':
    print(" View Employee Details")
    sql = "Select*from employee"
    mycursor.execute(sql,)
    result = mycursor.fetchall()
    for r in result:
        print(r)
    print("Employee Details successfully view")

elif choose == '6':
    print("View Attendance Report")
    a = input("Enter Employee_id:")
    sql = "Select*from attendance_report where Employee_id= %s"
    val = (a,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    if result:
     for t in result:
        print(t)
     print("Attendance report successfully view")
    else:
        print("Not found Attendance report ! Try Again")

elif choose == '7':
    print("View Salary Report")
    a = input("Enter Employee_id:")
    sql = "Select*from salary_payment where Employee_id= %s"
    val = (a,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    if result:
     for s in result:
        print(s)
     print("Salary report successfully view")
    else:
        print("Not found salary report ! Try Again")

elif choose == '8':
    print("View Leave Requests")
    sql = "Select*from leave_requests"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        print(x)
    print("All leave requests view successfully")

elif choose == '9':
    print("Manage Leave Requests")
    sql = "select*from leave_requests"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for y in res:
        print(y)

    g = input("Enter Employee_id to manage leave request:")
    sql = "select*from leave_requests where Employee_id = %s"
    val = (g,)
    mycursor.execute(sql,val)
    shu = mycursor.fetchall()
    if shu:
     for x in shu:
        print(x)            
    else:
        print("Employee_id not found in leave requests.")  
        exit()         

    h = input("Enter leave_status to manage:(Pending, Approved, or Rejected)")
    if h == "Pending" or h ==  "Approved" or  h == "Rejected":
        sql = "Update leave_requests Set Status = %s where Employee_id = %s"
        val = (h,g)
        mycursor.execute(sql,val)
        db.commit()
        print("Leave requests Manage successfully")
    else:
        print("Wrong Status Enter ! Enter Correct Status")
else:
    print("Sorry !! You are choose wrong option . Terminal is exit !! THANK YOU")       
print("Terminal Closed !! THANK YOU !!")
     


    
 
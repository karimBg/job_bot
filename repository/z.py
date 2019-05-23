import pyodbc

cnxn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=BackEndDb;"
    "Trusted_Connection=yes;"
)

cursor = cnxn.cursor()

# query 1:
response = cursor.execute(f"SELECT Title FROM jobs WHERE IdUserDb='5587499e-a518-4303-946c-cc9fc96b5bba'")

possible_jobs = []
for row in response:
    # result = "%r" % row
    possible_jobs.append({"jobRef": row[0]})

# print(possible_jobs)
# print(result[2 : len(result) - 4])

description = "description"

# query 2:
query = cursor.execute(f"SELECT {description.capitalize()} FROM jobs WHERE Title='designer' AND IdUserDb='5587499e-a518-4303-946c-cc9fc96b5bba'")
for row in query:
    job_data = row[0]

# print(job_data)

# query 3:
import datetime

def db_access_option(select_option):
    select_option = select_option.lower()
    if(select_option == "procedure"):
        select_option = "ApplicationProcedure"
    elif("date" in select_option):
        select_option = "OpeningDate"
    elif("deadline" in select_option):
        select_option = "ApplicationDeadline"
    return select_option

def execute_query_stmt(query_option, query_table):
    stmt = f"SELECT {query_option} FROM {query_table} WHERE Title='designer' AND IdUserDb='5587499e-a518-4303-946c-cc9fc96b5bba'"
    query = cursor.execute(stmt)
    return query

def query_data(query_option):
    # If We have the words: date or deadline we format the returned value
    if("date" in query_option.lower()) or ("deadline" in query_option.lower()):
        query_option = db_access_option(query_option)

        for row in execute_query_stmt(query_option, "jobs"):
            # format the date
            print(type(row[0]))
            result = row[0].strftime('%d-%m-%Y')
    else:
        for row in execute_query_stmt(query_option.capitalize(), "jobs"):
            # Don't format anything
            result = row[0]
    return result

# query_option = db_access_option("opening date")

# query = cursor.execute(f"SELECT {query_option} FROM jobs WHERE Title='designer' AND IdUserDb='5587499e-a518-4303-946c-cc9fc96b5bba'")

# query_data("date")


# def list_internships(user_id):
#    internships = cursor.execute(f"SELECT Title, RefInternship FROM internships WHERE IdUserDb='{user_id}'")

#    possible_internships = []
#    for row in internships:
#       possible_internships.append({
#       "internshipRef": row[1],
#       "Internship Title": row[0]
#       })

#    return possible_internships

<<<<<<< HEAD
# result = list_internships("5587499e-a518-4303-946c-cc9fc96b5bba")

# print(result)
# 5587499e-a518-4303-946c-cc9fc96b5bba
# dfac1d50-83ff-4073-95eb-4e12ac800b9c
# [-]a518[-]4303[-]946c[-]cc9fc96b5bba"
import datetime

userId = "5587499e-a518-4303-946c-cc9fc96b5bba"
Experience_years = "1"
Apply_date = datetime.datetime.now()
# query.execute("SET IDENTITY_INSERT Applicant ON")
query = cursor.execute(f"INSERT INTO Applicant( Name, Experience_years, Apply_date, IdUserDb) VALUES ('islem', {Experience_years}, '{Apply_date}', '{userId}')")
cnxn.commit()
=======
print(result)

def getRoleID(sub_role):
    i =100
    if(sub_role=="Network and Security"):
        i=8
    elif(sub_role=="Product Marketing"):
        i=7
    elif(sub_role=="Digital Marketing"):
        i=3
    elif(sub_role=="Back-End Development"):
        i=1
    elif(sub_role=="Front-End Development"):
        i=0
    elif(sub_role=="Fullstack"):
        i=2
    if(sub_role=="UI"):
        i=4
    elif(sub_role=="UX"):
        i=5
    elif(sub_role=="UI/UX"):
        i=6
    return i 
>>>>>>> 8c71d2594e32ed11480e2ade92cccb380f0d5d94

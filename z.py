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
    possible_jobs.append({"job_title": row[0]})

print(possible_jobs)
# print(result[2 : len(result) - 4])

description = "description"

# query 2:
query = cursor.execute(f"SELECT {description.capitalize()} FROM jobs WHERE Title='designer' AND IdUserDb='5587499e-a518-4303-946c-cc9fc96b5bba'")
for row in query:
    job_data = row[0]

print(job_data)
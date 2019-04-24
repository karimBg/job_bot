import pyodbc

cnxn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=BackEndDb;"
    "Trusted_Connection=yes;"
)

cursor = cnxn.cursor()

response = cursor.execute("SELECT Description FROM jobs WHERE Title = 'designer'")

for row in response:
    result = "%r" % row

print(result[2 : len(result) - 4])


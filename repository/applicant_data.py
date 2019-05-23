import datetime

from repository.data_access import cursor ,cnxn

def saveApplicantData(self, jobRef ,Name, Experience_years, Phone_number, Email, cv_link , IdUserDb):
    cursor.execute('''
                INSERT INTO Applicant VALUES (2,{jobRef}, Name, Experience_years, Phone_number, Email, cv_link, datetime.datetime.now() ,IdUserDb, 0)
                ''')
    cnxn.commit()
    print("it worked maybe ?")

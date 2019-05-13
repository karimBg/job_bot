from repository.data_access import cursor
import datetime

def db_access_option(select_option):
   if(select_option == "procedure"):
      select_option = "ApplicationProcedure"
   elif(select_option == "date"):
      select_option = "OpeningDate"
   elif(select_option == "deadline"):
      select_option = "ApplicationDeadline"

   return select_option

def get_job_data(job_option, job_title, user_id):
   job_option = db_access_option(job_option)
   query = cursor.execute(f"SELECT {job_option.capitalize()} FROM jobs WHERE Title='{job_title}' AND IdUserDb='{user_id}'")

   for row in query:
      job_data = row[0]

   if(type(job_data) is datetime.datetime):
      return job_data.strftime('%d/%m/%Y')

   return job_data
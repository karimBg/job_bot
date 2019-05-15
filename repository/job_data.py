import datetime

from repository.data_access import cursor

# Creates a list out of all existing jobs for a specific user.
def list_jobs(user_id):
   jobs = cursor.execute(f"SELECT Title FROM jobs WHERE IdUserDb='{user_id}'")

   possible_jobs = []
   for row in jobs:
      possible_jobs.append({"job_title": row[0]})
   
   return possible_jobs

#  transforms an option specified by the user to one we can query the DB with.
def transform_option(select_option):
   if(select_option == "procedure"):
      select_option = "ApplicationProcedure"
   elif(select_option == "mission"):
      select_option = "Responsibilities"
   elif(select_option == "date"):
      select_option = "OpeningDate"
   elif(select_option == "deadline"):
      select_option = "ApplicationDeadline"

   return select_option

# Gets all the data for a specific job and for a specific option.
def get_job_data(job_option, job_title, user_id):
   job_option = transform_option(job_option)
   query = cursor.execute(f"SELECT {job_option.capitalize()} FROM jobs WHERE Title='{job_title}' AND IdUserDb='{user_id}'")

   for row in query:
      job_data = row[0]

   if(type(job_data) is datetime.datetime):
      return job_data.strftime('%d/%m/%Y')

   return job_data
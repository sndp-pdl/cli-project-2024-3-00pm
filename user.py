import csv 
import sqlite3


def create_connection():
  try:
    con=sqlite3.connect('users.sqlite3')
    return con 
  except Exception as e:
    print(e)

INPUT_STRING='''
  enter the option:
  1. create table
  2. DUMP users from CSV into users table
  3. add new user into users table
  4. query all the users from the table 
  5. query user by id from table
  6. query specified no.of records from the table
  7. delete all the users 
  8. update user by id 
  9. update user 
  10.press any key to exit
  

'''
def create_table(con):
  create_users_table_query='''
    create table if not exists users(
    id integer primary key autoincrement,
    first_name char(255) not null,
    last_name char (255) not null,
    company_name char(255) not null, 
    address char(255) not null, 
    city char(255) not null, 
    county char(255) not null, 
    state char(255) not null, 
    zip real not null, 
    phone1 char(255) not null, 
    phone2 char(255) not null, 
    email char(255) not null,
    web text 
                       
    );
  '''
  cur=con.cursor()
  cur.execute(create_users_table_query)
  print('users table was created sucessfully.')

def read_csv():
  users = []
  with open ('sample_users.csv','r') as f:
    data = csv.reader(f)
    for user in data:
      users.append(tuple(user))
  return users[1:]
      
      
def insert_users(con,users):
  user_add_query='''
  INSERt into users
  (
   first_name,
   last_name,
   company_name,
   address,
   city,
   county,
   state,
   zip,
   phone1,
   phone2,
   email,
   web
   
   )
     values(?,?,?,?,?,?,?,?,?,?,?,?);
  
  '''
  cur=con.cursor()
  cur.executemany (user_add_query, users)
  con.commit()
  print(f'{len(users)}users were imported sucessfully.')


def select_users(con,no_of_users=None):
  cur=con.cursor()
  if no_of_users:
    users=cur.execute(f' select * from users limit {no_of_users}')
  else :
    users =cur.execute ('select * from users')
  for user in users:
    print(user)


def select_user_by_id(con,user_id):
  cur=con.cursor()
  users=cur.execute('select * from users where id=?;'(user_id,))
  for user in users:
    print(user)



def delete_users(con):
  cur=con.cursor()
  cur.execute('delete from users;')
  con.commit()
  print('All users were deleted sucessfully')
        


def delete_user_by_id(con,user_id):
  cur=con.cursor()
  cur.eecute('DELETE FROM users where id=?',(user_id))
  con.commit()
  print(f'user with id[{user_id}]was sucessfully deleted.')


COLUMNS =(
  'first_name',
  'last_name',
  'company_name',
  'address',
  'city',
  'county',
  'state',
  'zip',
  'phone1',
  'phone2',
  'email',
  'web',
)





def main():
  con=create_connection()
  if con:
    user_input=input(INPUT_STRING)
    if user_input =='1':
      create_table(con)
    elif user_input =='2':
      users=read_csv()
      insert_users(con,users)
    elif user_input =='3':
      user_data=[]
      for column in COLUMNS:
        column_value=input(f'Enter the value of{column}:')
        user_data.append(column_value)
        insert_users(con,[tuple(user_data)])
    elif user_input =='4':
      select_users(con)

    elif user_input =='5':
      user_id=input('enter user id:')
    if user_id.isnumeric():
        select_users_by_id(con,user_id)
    else:
      print('invalid user id. exiting...')
  elif user_input =='6':
   no_of_users =input('enter no. of users:')
  
   if no_of_users.isnumeric():
        select_users(con,no_of_users)
  elif user_input =='7':
      conformation=input ('are you sure you want to delete all users? (y/n):')
  if conformation.lower() in['y','yes']:
        delete_users(con)
  elif user_input =='8':
    user_id=input('enter user id:')
    if user_idisnumeric():
      delet_user_by_id(con,user_id)
  elif user_input== '9':
    user_id = input('enter id of user:')
    if  user_id.ismuneric():
     column_name=input(
      f'enter the column you want to edit .Please make sure column is within {COLUMNS}:'
)
    if coloumn_name in COLUMNS:
      column_value=input(f'enter the value of {column_name}:')
      update_user_by_id(con, user_id, column_name, column_value)

    else :
      exit()


  
main()




  

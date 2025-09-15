import pyodbc
from getconnectionstring import connectionstring
import datetime
import json
import calendar
import decimal
def get_connection():
        
        try:
                cnxn = pyodbc.connect(connectionstring)
                print("Connected to the database!")
                return cnxn.cursor(), cnxn
        except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                if sqlstate == 'HY000':
                        print(f"Connection failed: {ex}")
                else:
                        print(f"An error occurred: {ex}")
                exit()




def get_dashboard():
    cursor, cnxn = get_connection()
    current_date = datetime.date.today()
    current_month_name = current_date.strftime('%B')
    last_day = calendar.monthrange(current_date.year, current_date.month)[1]
    month_end_date = datetime.date(current_date.year, current_date.month, last_day)

    data = {}
    birthday_list = []

    try:
        # 1️⃣ Active student count
        cursor.execute("""
            SELECT COUNT(*) 
            FROM students 
            WHERE is_active=1
        """)
        activestudentresult = cursor.fetchone()
        activestudent = activestudentresult[0] if activestudentresult else 0
        data["activestudentdata"] = activestudent

        # 2️⃣ Birthdays in current month
        cursor.execute("""
            SELECT first_name, last_name, date_of_birth 
            FROM students 
            WHERE MONTH(date_of_birth) = ? 
              AND DAY(date_of_birth) BETWEEN ? AND ?
        """, (current_date.month, current_date.day, month_end_date.day))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                birthday_list.append([row.first_name, row.last_name, row.date_of_birth])

        '''# 3️⃣ Top students by amount
        cursor.execute("""
            SELECT first_name, SUM(amount) AS total_amount 
            FROM payments 
            GROUP BY first_name 
            ORDER BY total_amount DESC
        """)'''
        '''student_dict = {}
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                student_dict[row.first_name] = row.total_amount
            sorted_dict_desc = dict(sorted(student_dict.items(), key=lambda item: item[1], reverse=True))
            data["top_students"] = sorted_dict_desc

        # 4️⃣ Group-wise expenses
        cursor.execute("""
            SELECT expense_type, SUM(cost) AS total_cost 
            FROM expenses 
            WHERE YEAR(expense_date) = ? 
            GROUP BY expense_type
        """, (current_date.year,))
        rows = cursor.fetchall()
        groupWisedict = {}
        if rows:
            for row in rows:
                groupWisedict[row.expense_type] = row.total_cost
            data["groupwise_expenses"] = groupWisedict'''

    except pyodbc.ProgrammingError as e:
        print("Programming error occurred:", e)
    finally:
        cnxn.commit()
        cursor.close()
        cnxn.close()

    return data, birthday_list

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "lokesh139094",
    database = "note_db"
)
# print("connection done successfully!")

cursor = connection.cursor()

# Add a new note

def add_newnote():
    try:
        input_add_title = input("Enter the title for the new Note: ")
        input_add_content = input("Enter the content for the new Note: ")
        
        check_query = "SELECT * FROM notes WHERE Content = %s or Title = %s"
        cursor.execute(check_query, (input_add_content,input_add_title))
        
        result = cursor.fetchone()
        
        if result:
            print("Note already Exist!! kindly verify the table!")
        else:
            cursor.execute("INSERT INTO notes(Title, Content) values (%s, %s)",(input_add_title, input_add_content))
            connection.commit()

            print("New Note Added Successfully!!!")
        
    except mysql.connector.Error as Error:
        print("Something went wrong while adding a new note pls try again!")
    
    finally:
        print("Thank you!!!")
        
# View all notes

def view_note():
    
    try:
        cursor.execute("Select * from Notes")
        Notes = cursor.fetchall()
    
        for note in Notes:
            print("******************")
            print("Note_Id: ", note[0])
            print("Title: ", note[1])
            print("Content: ",note[2])
            print("******************")
    
    except mysql.connector.Error as Error:
        print("Something went wrong unable to view the notes kindly pls try again!")
    
    finally:
            print("Thank you!!!")
            
# Update a note

def update_note():
    try:
        old_title = input("Enter the current title of the note: ")

        print("\nWhat do you want to update?")
        print("1. Title")
        print("2. Content")
        print("3. Both")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_title = input("Enter the new title: ")
            
            # First check whether content exists
            check_query = "SELECT * FROM notes WHERE Title = %s"
            cursor.execute(check_query, (old_title,))

            result = cursor.fetchone()

            if result:

                queryUT = "UPDATE notes SET Title = %s, Updated_Date = current_timestamp() WHERE Title = %s"
                valuesUT = (new_title, old_title)
                
                cursor.execute(queryUT, valuesUT)
                
                print("Note updated successfully!")
                
            else:
                print("No such Note found!")

        elif choice == "2":
            new_content = input("Enter the new content: ")

            # First check whether content exists
            check_query = "SELECT * FROM notes WHERE Title = %s"
            cursor.execute(check_query, (old_title,))

            result = cursor.fetchone()

            if result:
            
                queryUC = "UPDATE notes SET Content = %s, Updated_Date = current_timestamp() WHERE Title = %s"
                valuesUC = (new_content, old_title)
                
                cursor.execute(queryUC, valuesUC)
                
                print("Note updated successfully!")
                
            else:
                print("No such Note found!")
                
        elif choice == "3":
            new_title = input("Enter the new title: ")
            new_content = input("Enter the new content: ")
            
            # First check whether content exists
            check_query = "SELECT * FROM notes WHERE Title = %s"
            cursor.execute(check_query, (old_title,))

            result = cursor.fetchone()

            if result:

                queryUTC = """
                UPDATE notes
                SET Title = %s, Content = %s, Updated_Date = current_timestamp()
                WHERE Title = %s
                """
                valuesUTC = (new_title, new_content, old_title)
                
                cursor.execute(queryUTC, valuesUTC)
                
                print("Note updated successfully!")
                
            else:
                print("No such Note found!")

        else:
            print("Invalid choice")
            pass

        connection.commit()

    except Exception:
        print("Something went wrong while updating the notes Kindly please try again!")
    finally:
        print("Thank you!!!")

# Delete a note

def delete_note():
    try:
        print("1. Delete by title")
        print("2. Delete by content")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
        
            title = input("Enter the title: ")
            
            # First check whether content exists
            check_query = "SELECT * FROM notes WHERE Title = %s"
            cursor.execute(check_query, (title,))
            
            result = cursor.fetchone()
            
            if result:
        
                queryt = "DELETE FROM notes WHERE Title = %s"
                valuest = (title,)
            else:
                print("No such Note found!")
                    
            cursor.execute(queryt, valuest)
            
            if cursor.rowcount > 0:
                print("Note deleted successfully!")
            else:
                print("Note not found!")
            
            
        
        elif choice == "2":
        
            content = input("Enter the content: ")
        
            # First check whether content exists
            check_query = "SELECT * FROM notes WHERE Content = %s"
            cursor.execute(check_query, (content,))

            result = cursor.fetchone()

            if result:
        
                queryc = "DELETE FROM notes WHERE Content = %s"
                valuesc = (content,)
            else:
                print("No such Note found!")
            
            cursor.execute(queryc, valuesc)
            
            if cursor.rowcount > 0:
                print("Note deleted successfully!")
            else:
                print("Note not found!")

        else:
            print("Invalid choice")
            
        connection.commit()
        
    except Exception as error:
        print("Something went wrong while try to delete the note kindly please try again!")
    finally:
        print("Thank you!!!")

# run a while loop to call the functions again

while True:
    try:
        
        print("\n===== NOTES SAVER =====")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Update a note")
        print("4. Delete a note")
        print("5. Exit")
        print("=======================")

        a= int(input("enter Your Choice: "))

        if a==1:
            add_newnote()
        elif a==2:
            view_note()
        elif a==3:
            update_note()
        elif a==4:
            delete_note()
        elif a==5:
            print("Note saver as been Exited!!")
            print("Thank you!!!")
            print("******************")
            break
        else:
            print("Invalid choice!!!")
    except Exception:
        
        
        print("Something Went wrong!!!") 
        
cursor.close
connection.close
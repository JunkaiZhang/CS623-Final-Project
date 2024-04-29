#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install psycopg2-binary


# In[2]:


#pip install --upgrade pip


# In[1]:


import psycopg2

try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="class",
        user="Junkai",
        password="123123",
        host="localhost",  
        port="5432"
    )
    # Create a cursor object
    cur = conn.cursor()
    print("Connected to the database successfully.")
except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")


# In[2]:


#show tables
try:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cur.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

except Exception as e:
    print("Error:", e)


# In[4]:


try:
    # 1. Delete product p1 from product and stock table
    # Delete product p1 from stock table
    cur.execute("DELETE FROM stock WHERE prod = 'p1';")

    # Delete product p1 from product table
    cur.execute("DELETE FROM product WHERE prod = 'p1';")

    conn.commit()
    print("Delete Completed: Product p1 deleted from Product and Stock tables.")
except Exception as e:
    conn.rollback()
    print(f"Transaction 1 failed: {e}")
    


# In[5]:


try:
    # 2. The depot d1 is deleted from Depot and Stock.
    # Delete d1 from the Stock table
    cur.execute("DELETE FROM stock WHERE dep = 'd1';")

    # Delete d1 from the Depot table
    cur.execute("DELETE FROM depot WHERE dep = 'd1';")

    conn.commit()

    print("Deletion successful: Depot d1 deleted from Depot and Stock tables.")
except Exception as e:
    conn.rollback()
    print(f"Transaction 2 failed: {e}")


# In[6]:


cur.close()
conn.close()


# In[ ]:





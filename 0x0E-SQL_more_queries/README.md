# 0x0E. SQL - More queries

# Concepts

1. How to create a new MySQL user:
    
    Creating a new user in MySQL involves using the CREATE USER statement, which can be executed by a user with administrative privileges. Here is an example of the syntax for creating a new user with a password:
    
    ```sql
    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
    ```
    
    This statement creates a new user called "newuser" who can only connect from the localhost, and assigns the user a password of "password". Once the user is created, you can then grant them permissions to access databases or tables.
    
2. How to manage privileges for a user to a database or table:
    
    MySQL privileges can be managed using the GRANT and REVOKE statements. These statements allow you to give or take away certain permissions from a user on a database or table. Here is an example of the syntax for granting a user all privileges on a specific database:
    
    ```sql
    GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
    ```
    
    This statement grants all privileges to the user "username" for the database called "database_name". You can also use these statements to grant specific privileges (such as SELECT, INSERT, UPDATE, or DELETE) on specific tables.
    
3. What’s a PRIMARY KEY:
    
    A PRIMARY KEY is a column or set of columns in a table that uniquely identifies each row in that table. This means that no two rows in the table can have the same values in the primary key column(s). The primary key is used to enforce data integrity and to establish relationships between tables (using FOREIGN KEYS, as explained below).
    
4. What’s a FOREIGN KEY:
    
    A FOREIGN KEY is a column or set of columns in a table that references the primary key of another table. This establishes a relationship between the two tables, where the values in the foreign key column(s) must match the values in the primary key column(s) of the other table. This is used to ensure data consistency and to enforce referential integrity between related tables.
    
5. How to use NOT NULL and UNIQUE constraints:
    
    The NOT NULL constraint ensures that a column in a table cannot contain null values, meaning that a value must be provided for that column when a new row is inserted. The UNIQUE constraint ensures that no two rows in the table can have the same value in that column. Here is an example of the syntax for adding these constraints to a table:
    
    ```sql
    CREATE TABLE table_name (
        column1 datatype NOT NULL,
        column2 datatype UNIQUE,
        ...
    );
    ```
    
6. How to retrieve data from multiple tables in one request:
    
    You can retrieve data from multiple tables using JOIN statements. A JOIN combines rows from two or more tables based on a related column between them. Here is an example of a simple JOIN statement that retrieves data from two tables:
    
    ```sql
    SELECT *
    FROM table1
    JOIN table2
    ON table1.column = table2.column;
    ```
    
    This statement joins the rows from table1 and table2 where the values in the "column" column match, and returns all columns from both tables.
    
7. What are subqueries:
    
    A subquery is a query that is embedded within another query. Subqueries can be used to retrieve data that will be used in the main query, or to filter the results of the main query based on some condition. Here is an example of a simple subquery that retrieves data based on a condition:
    
    ```sql
    sqlCopy code
    SELECT column1
    FROM table1
    WHERE column2 IN (SELECT column2 FROM table2 WHERE condition);
    ```
    
    This statement retrieves data from table1 where the values in "column2" are also in table2 and match some condition.
    
8. What are JOIN and UNION:
    
    As mentioned earlier, JOIN is a method for combining rows from two or more tables based on a related column between them. There are several types of JOIN, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN. Each type of JOIN has its own specific syntax and behavior.
    
    On the other hand, UNION is used to combine the results of two or more SELECT statements into a single result set. The result set of a UNION operation contains all the distinct rows from each SELECT statement. Here is an example of the syntax for using UNION:
    
    ```sql
    SELECT column1 FROM table1
    UNION
    SELECT column1 FROM table2;
    ```
    
    This statement retrieves the values of "column1" from both table1 and table2, and combines them into a single result set with no duplicates.
    
    In summary, MySQL is a powerful database management system that allows users to create new users, manage privileges, establish relationships between tables, enforce data integrity, and retrieve data from multiple tables in a single query using JOIN statements or subqueries. UNION is used to combine the results of multiple SELECT statements into a single result set.

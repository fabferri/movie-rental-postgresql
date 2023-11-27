<properties
pageTitle= 'PostgreSQL: introduction'
description= "PostgreSQL: introduction"
documentationcenter: na
services=""
documentationCenter="github"
authors="fabferri"
manager=""
editor=""/>

<tags
   ms.service="howto-Azure-examples"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="PostgreSQL"
   ms.date="27/09/2023"
   ms.review=""
   ms.author="fabferri" />

# PostgreSQL: introduction
The article is a basic introduction to PostgreSQL.

### <a name="connect to postgre"></a>1.1 Connect to the local PostgreSQL
After postGreSQL installation, to establish a connection with the newly set-up database, log into the **postgres** account and open a postgress prompt:
```bash
sudo su - postgres 

psql
```

To check the connection to PostgreSQL and the TCP port (default is 5432):
```bash
\conninfo
```

### <a name="Create user and DB"></a>1.2 PosteGre roles 
PostgreSQL roles enable you to control the access and capabilities of users who access a PostgreSQL instance. <br>
PostgreSQL roles can be a single role, or they can function as a group of roles. A user is a role with the ability to log in (the role has the LOGIN attribute) <br>
By default, when PostgresSQL server is created, the only user that exists is **postgres**. <br>
The **postgres** user is the most highly privileged database user.<br>

Users, groups, and roles are the same thing in PostgreSQL, with the only difference being that users have permission to log in by default. The **CREATE USER** and **CREATE GROUP** statements are actually aliases for the CREATE ROLE statement. <br>


To create a PostgreSQL user, use the following SQL statement:
```sql
CREATE USER your_username WITH PASSWORD 'your_password';
```
You can also create a user with the following SQL statement:
```sql
CREATE ROLE your_username WITH LOGIN PASSWORD 'your_password';
```
Both of these statements create the exact same user. This new user does not have any permissions other than the default permissions available to the public role.
When a role with the **LOGIN** attribute is created, it can log into the PostgreSQL database server. However, it cannot interact with the database objects until privileges are granted to that role. <br>


Create a role that can <ins>create databases</ins> and <ins>manage roles</ins>:
```sql
CREATE ROLE admin WITH CREATEDB CREATEROLE;
```
Create a new user with password and assign the role **CREATEDB**:
```sql
CREATE ROLE your_username CREATEDB LOGIN PASSWORD 'your_password';
```
The role can take the following values: 
* **SUPERUSER** | **NOSUPERUSER** – determine if the role is a superuser or not. Superusers can change any of those attributes for any role.
* **CREATEDB** | **NOCREATEDB** – allow the role to create new databases.
* **CREATEROLE** | **NOCREATEROLE** – allow the role to create or change roles.
* **INHERIT** | **NOINHERIT** – determine if the role to inherit privileges of roles of which it is a member.
* **LOGIN** | **NOLOGIN** – allow the role to log in.
* **REPLICATION** | **NOREPLICATION** – determine if the role is a replication roles.
* **BYPASSRLS** | **NOBYPASSRLS** – determine if the role to by pass a row-level security (RLS) policy

Delete a role:
```sql
DROP ROLE your_username;
```

To determine the set of existing roles:
```sql
SELECT rolname FROM pg_roles;
```
List of existing roles:
```sql
\du+
```

On PostgreSQL server creating database, create a role, grant to the role access to the database with all priviledges:
```sql
sudo -u postgres psql
postgres=# CREATE DATABASE db_name;
postgres=# CREATE ROLE your_role LOGIN ENCRYPTED PASSWORD 'your_password' ;
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_name TO your_role ;
```

Give to the role the ability to connect to the database:
```sql
GRANT CONNECT ON DATABASE db_name TO your_role;
```

Grant these the your_username the privileges associated with the your_role:
```sql
GRANT your_role TO your_username;
```
At this point, your_username a can connect to the database db_name

A way to create a role user if not-exists:
```sql
DO
$$
BEGIN
  IF NOT EXISTS (SELECT * from pg_user WHERE usename = 'new_role') THEN
     CREATE ROLE new_role WITH LOGIN PASSWORD 'your_password';
  END IF;
END
$$ ;
```

Changing the user permission:
```sql
ALTER ROLE your_role WITH OPTION1 OPTION2 OPTION3;
```
The OPTION can takes the folloing values: **CREATEDB, CREATEROLE, CREATEUSER, SUPERUSER**. <br>
To deny the user that particular permission can be used: **NOCREATEDB, NOCREATEROLE, NOSUPERUSER**


To connect to the PostgreSQ locally:
```sql
psql -h localhost -d postgres -p 5432 -U your_username
```
To connect to the PostgreSQ remotly:
```sql
psql -h IP_server -d postgres -p 5432 -U username
```


### <a name="psql"></a>1.3 Install PostgreSQL client
PostgreSQL server installs automatically the PostgreSQL client.<br> 
For Ubuntu hosts/VMs without PostgreSQL server installed; the only PostgreSQL client can be installed by command:

```bash
sudo apt-get install postgresql-client
```
After completing the installation process, you should be able to run psql in the terminal/command prompt to connect to your PostgreSQL database.

### <a name="Connect to a remote PostgreSQL"></a>1.4 Connect to a remote PostgreSQL
By default PostgreSQL allows access from localhost. Few changes need to be applied to enable remote access.
- Open the file **/etc/postgresql/16/main/postgresql.conf** in PostgreSQL server and change inside the statement **#listen_addresses = 'localhost'** into **listen_addresses = '*'**. 
- Open the file **/etc/postgresql/16/main/pg_hba.conf** in PostgreSQL server and add this line to that file: <br>
```sql
host    all             all             0.0.0.0/0               md5
```
It allows access to all databases for all users with an encrypted password. <br>
When done, restart the PostgreSQL: **systemctl restart postgresql** <br>

<br>

To connect to a remote postgreSQL database, without prompt for password can be used few methods:

* method 1: <ins>define the **PGPASSWORD** environment variable</ins>: 
```bash
export PGPASSWORD=<yourpass>
psql -h URI -d postgres -p 5432 -U username
```
-d specify the DB <br>
-p specifies the TCP port (default value is 5432) <br>

* method 2: <ins>login specifing the password on single line</ins>: 
```bash
PGPASSWORD=your_password psql -h URI -d postgres -p 5432 -U username
OR
PGPASSWORD=your_password psql -h IP_servername -d postgres -p 5432 -U username
```

### <a name="Connect to a remote PostgreSQL"></a>1.5 run a PostgreSQL script

PGPASSWORD=your_password psql -h 127.0.0.1 -d postgres -p 5432 -U username

### <a name="create user and DB"></a>1.5 Few PostgreSQL commands
Check the PostgreSQL version:
```sql
SELECT version();
```

Create a Database is not exists:
```sql
SELECT 'CREATE DATABASE movies'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'movies')\gexec 
```

NOTE: <br>
\gexec  sends the current query buffer to the server, then treats each column of each row of the query's output (if any) as a SQL statement to be executed.

Delete database:
```sql
DROP DATABASE db_name;
```

Delete table if exists:
```sql
DROP TABLE IF EXIST table_name [CASCADE | RESTRICT];
```
- In case the table that you want to remove is used in views, constraints, or any other objects, the **CASCADE** allows users to remove those dependent objects together with the table automatically.
- **RESTRICT** refuses to drop table if there is any object depends on it. PostgreSQL uses **RESTRICT** by default.


In PostgreSQL, the structure of an existing table can be modified using the ALTER TABLE statement.
```sql
ALTER TABLE table_name action;
```

- Add a column to an existing table:
```sql
ALTER TABLE table_name ADD COLUMN new_column_name TYPE;
```

- Drop a column from an existing table:
```sql
Drop a column from an existing table
```

- Rename an existing table:
```sql
ALTER TABLE table_name RENAME TO new_table_name;
```

- Rename a column from an existing table:
```sql
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
```

- List of databases: **\l**
- List tables in your database: **\d**
- To connect to a db: **\c** *db_name*
- Check for all available tables in the database: **\dt**
- Describe a table: **\d** `<tablename>`
- List all schemas: **\dn**
- List all user accounts (or roles) and permission: **\du** 



`Tags: PostgreSQL` <br>
`date: 27-11-23`

<!--Image References-->

[1]: ./media/db-schema.png "db schema"
[2]: ./media/network-diagram-details.png "network diagram with details"
[3]: ./media/datapaths.png "data flows transit"
[4]: ./media/effective-routes.png "effective routes"


<!--Link References-->


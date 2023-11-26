

<properties
pageTitle = 'Movie Rental in PostgreSQL'
description = "Movie Rental in PostgreSQL"
documentationcenter: na
services = "PostgreSQL"
documentationCenter = "github"
authors = "fabferri"
editor = ""/>

<tags
   ms.service = "Example of PostgreSQL"
   ms.devlang = "na"
   ms.topic = "DB"
   ms.tgt_pltfrm = "linux, windows"
   ms.workload = "PostgreSQL"
   ms.date = "26/11/2023"
   ms.author = "fabferri" />

# Movie rental in PostgreSQL
The Entity Relationship (ER) diagram is shown below:

[![1]][1]


## <a name="list of files"></a>1. File list

| File name             | Description                                                                             |
| --------------------- | --------------------------------------------------------------------------------------- |
| **movies .sql**       | generate the DB **movies**                                                              |
| **users.sql**         | generate the reconrds in the table **customer**                                         |
| **payment.sql**       | generate the transaction for movie rental                                               |
| **generate-users.py** | python script to generate the file **user.sql**. run the file only if you want to generate other users. the fist name, last name, address are randomly generated |

`Tags:PostgreSQL` <br>
`date: 16-11-2023`

<!--Image References-->

[1]: ./media/er-diagram.png "Entity Relationship (ER) diagram"


<!--Link References-->
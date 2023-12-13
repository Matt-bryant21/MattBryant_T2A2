# Matt Bryant T2A2 API Webserver Project
![UFC Fighter Management System](/docs/UFC%20Fighter%20Management%20System.png)

## R1 Identification of the problem you are trying to solve by building the app
The Ultimate Fighting Championship (UFC) is not just a premier mixed martial arts organization; it's a billion-dollar empire that orchestrates the careers of over 500 fighters across 12 divisions. In this high-stakes arena, each fighter's record is a dynamic entity, susceptible to rapid changes through regular and almost weekly events. The problem at hand involves several intricate aspects:

* Dynamic Fighter Records: Fighter records in the UFC are constantly evolving. Each event can significantly alter a fighter's career trajectory, making it crucial to update records swiftly to reflect these changes accurately.

* High Fan Engagement and Expectations: The UFC's passionate fanbase demands up-to-date information. Fans actively engage in discussions and predictions about future matchups and championships, necessitating immediate updates to fighter records following events.

* Complex Data Management: The sheer volume of fighters and the frequency of events create a logistical challenge in maintaining accurate and current records. There's a need for a system that can efficiently manage the creation, updating, and deletion of these records in a centralised platform.

__The Solution: A Specialized Web Application for UFC Fighter Management__

The purpose of developing this web application is to address these specific problems by:

* Offering Real-Time Updates: The app will enable quick updates to fighter records, keeping pace with the rapid changes that occur in the UFC, thus maintaining data integrity.

* Enhancing User Interaction: By providing a clean and simple interface, the app allows users, ranging from fans to professionals, to interact with the latest fighter records easily.

* Facilitating Data Control and Security: Depending on their privileges, users can not only view but also modify fighter records. This includes adding new records, updating existing ones, and, where necessary, deleting them.

By tackling these problems, the app aims to streamline the management of fighter records, cater to the high expectations of UFC fans, and enhance the operational efficiency of managing fighter data. 

## R2 Why is it a problem that needs solving? 
The world of mixed martial arts, particularly in organizations like the UFC, represents a vast and complex ecosystem. At its core, athlete management in such a high-profile sport is a colossal undertaking, encompassing a range of critical aspects:

* Volume of Athletes: With hundreds of fighters across multiple weight divisions, each with unique career trajectories, keeping track of every athlete's record, health status, contractual obligations, and ranking is a Herculean task.

* Dynamic Nature of Fighter Records: Fighter profiles are not static; they evolve with each bout. This includes updates in win-loss records, performance metrics, and medical suspensions. Accurate and real-time tracking of these changes is vital for the integrity of the sport.

* Fan Engagement and Transparency: Fans and analysts demand up-to-date information on fighter stats, upcoming bouts, and division rankings. Providing this information in a user-friendly manner enhances fan engagement and the sport's accessibility.

By creating an API that efficiently manages UFC fighter records and divisions, I am addressing these challenges head-on.

## R3 Why have you chosen this database system? What are the drawbacks compared to others?

Postgres frequently emerges as the top choice for Flask applications, largely owing to its robust library support through packages such as Psycopg2 and SQLAlchemy. These libraries facilitate strong scalability and ease the learning curve for database implementation. Additionally, the support for Object-Relational Mapping (ORM) significantly contributes to Postgres's appeal. By employing ORM, which seamlessly maps the models feeding data into the database, developers find a reduced learning curve and a notable increase in scalability. This integration streamlines database interactions, making Postgres an efficient and user-friendly choice for Flask-based applications.

Before choosing a DBMS it's important to consider other alternatives and assess potential drawbacks, regardless of how strong the initial appeal is. SQLite is another common relational database management system that is discussed below.

### Primary Differences

***Server-Client Model vs Embedded Database:***

* Postgres: Operates on a server-client model. It's a robust, multi-user DBMS that runs on a server and can be accessed remotely by multiple clients.

* SQLite: An embedded database, it's integrated directly into the application. It's lightweight and intended for single-user applications or small-scale projects.

***Performance and Scalability:***

* Postgres: Known for its high performance, especially in handling complex queries, large databases, and multiple concurrent users. It's highly scalable, making it suitable for large-scale enterprise applications.

* SQLite: Optimized for lower resource usage and is efficient for smaller-scale applications. However, it might not perform well with high concurrency or complex queries.

***Feature Set:***

* Postgres: Offers a wide range of features including advanced indexing, full-text search, data warehousing, and support for multiple programming languages. It also supports JSON and NoSQL features, catering to a wider range of applications.

* SQLite: Provides a simpler feature set, focusing on basic SQL standards. While it supports most of the common SQL functionalities, it lacks some advanced features found in Postgres.

***Data Integrity and Security:***

* Postgres: Offers robust data integrity and security features. It includes support for ACID (Atomicity, Consistency, Isolation, Durability) properties, complex transactional capabilities, and strong security measures.

* SQLite: While reliable for data integrity, its simpler nature means it lacks some of the more sophisticated security and transactional features present in Postgres.

### Why Prefer Postgres?

***Enterprise-Grade Capabilities:*** For large-scale, multi-user, enterprise-level applications, Postgres is the preferred choice due to its scalability, performance, and rich feature set.

***Complex Data Handling:*** Postgres excels in handling complex queries, diverse data types, and large data volumes, making it ideal for complex applications like data analytics and warehousing.

***Extension and Language Support:*** With its extensibility and support for various programming languages, Postgres is highly adaptable to a wide range of applications and development needs.


### Conclusion
While SQLite is an excellent choice for simpler, embedded database needs, Postgres stands out for applications that demand higher performance, scalability, and a comprehensive set of features. Its ability to handle complex, enterprise-level applications with efficiency and reliability makes Postgres a preferred choice for this application.

___Sources___

https://www.boltic.io/blog/postgresql-vs-sqlite#:~:text=SQLite%20may%20be%20the%20better,data%20and%20support%20advanced%20features.

https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems


## R4 Identify and discuss the key functionalities and benefits of an ORM


Object-Relational Mapping (ORM) offers a streamlined method for interacting with databases, bypassing the need for direct SQL query injection. By integrating ORM, users can harness the familiar paradigms of their programming language, such as creating classes, objects, instances, and methods. This approach aligns database operations with the language-specific structure, simplifying the process of data manipulation between the application and the database. This methodology not only saves time but also, once mastered, significantly simplifies coding for database interactions.

Benefits of using ORM include:

Language Consistency:

* ORM allows you to write database operations in the same programming language used in your application. For instance, in a Flask application, you can manage database interactions using Python objects instead of writing SQL queries. 

Leveraging Language Features:

* By using ORM, you gain access to advanced features and capabilities of the programming language in use. This includes taking advantage of language-specific libraries and packages, which can offer extended functionalities and tools that might not be readily available or as efficient when using raw SQL. For example, Python’s libraries like SQLAlchemy provide powerful ORM capabilities, enhancing the efficiency and scalability of database operations.


Improved Code Maintainability and Readability:

* Code that uses ORM tends to be more readable and maintainable. It abstracts the complexities of raw SQL queries into more intuitive and high-level programming constructs. This abstraction makes the code easier to understand, modify, and maintain, especially for developers who might not be experts in SQL.


___Sources___

https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a

https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/

## R5 Document all endpoints for your API


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 1**                      | `/users/register`                                               |
| **HTTP Request Verb**             | POST                                                            |
| **Required Data**                 | `username`, `password`, `role`                                  |
| **Expected Response Data**        | Message indicating successful registration                     |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role        |

![Endpoint1](/docs/endpoints/user%20registered.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 2**                      | `/users/login`                                                  |
| **HTTP Request Verb**             | POST                                                            |
| **Required Data**                 | `username`, `password`                                          |
| **Expected Response Data**        | Access token if credentials are valid                           |
| **Authentication Methods**        | None (open access)                                              |

![Endpoint 2](/docs/endpoints/login%20user.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 3**                      | `/users/view_user/<int:user_id>`                                |
| **HTTP Request Verb**             | GET                                                             |
| **Required Data**                 | `user_id` (in URL)                                              |
| **Expected Response Data**        | User information                                                |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role        |

![Endpoint 3](/docs/endpoints/view%20user.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 4**                      | `/users/update_user/<int:user_id>`                              |
| **HTTP Request Verb**             | PUT                                                             |
| **Required Data**                 | `user_id`, `current_password`, optional: `username`, `role`, `new_password` |
| **Expected Response Data**        | Confirmation message on successful update                       |
| **Authentication Methods**        | JWT required; User cannot update their own information          |

![Endpoint 4](/docs/endpoints/update%20user.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 5**                      | `/users/delete_user/<int:user_id>`                              |
| **HTTP Request Verb**             | DELETE                                                          |
| **Required Data**                 | `user_id`                                                       |
| **Expected Response Data**        | Confirmation message on successful deletion                     |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role        |

![Endpoint 5](/docs/endpoints/delete%20user.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 6**                      | `/fighters/add_fighter`                                         |
| **HTTP Request Verb**             | POST                                                            |
| **Required Data**                 | `name`, `age`, `height`, `weight`, `record`, `division_id`      |
| **Expected Response Data**        | Message indicating successful addition of fighter               |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role        |

![Endpoint 6](/docs/endpoints/create%20fighter.JPG)

| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 7**                      | `/fighters/view_fighter/<int:fighter_id>`                       |
| **HTTP Request Verb**             | GET                                                             |
| **Required Data**                 | `fighter_id` (in URL)                                           |
| **Expected Response Data**        | Fighter information                                             |
| **Authentication Methods**        | JWT required; Access limited to users with allowed roles        |

![Endpoint 7](/docs/endpoints/view%20fighter.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 8**                      | `/fighters/update_fighter/<int:fighter_id>`                     |
| **HTTP Request Verb**             | PUT                                                             |
| **Required Data**                 | `fighter_id`, `name`, `age`, `height`, `weight`, `record`, `division_id`|
| **Expected Response Data**        | Confirmation message on successful update                       |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' or 'referee' roles |

![Endpoint 8](/docs/endpoints/modify%20fighter.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 9**                      | `/fighters/delete_fighter/<int:fighter_id>`                     |
| **HTTP Request Verb**             | DELETE                                                          |
| **Required Data**                 | `fighter_id`                                                    |
| **Expected Response Data**        | Message indicating successful deletion                          |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role        |

![Endpoint 9](/docs/endpoints/delete%20fighter.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 10**                      | `/divisions/create_division`                                    |
| **HTTP Request Verb**             | POST                                                            |
| **Required Data**                 | `name`, `description`                                           |
| **Expected Response Data**        | Message indicating successful creation of the division          |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role         |

![Endpoint 10](/docs/endpoints/create%20division.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 11**                      | `/divisions/view_division/<int:division_id>`                    |
| **HTTP Request Verb**             | GET                                                             |
| **Required Data**                 | `division_id` (in URL)                                          |
| **Expected Response Data**        | Division information                                            |
| **Authentication Methods**        | JWT required; Access limited to users with allowed roles        |

![Endpoint 11](/docs/endpoints/view%20division.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 12**                      | `/divisions/update_division/<int:division_id>`                  |
| **HTTP Request Verb**             | PUT                                                             |
| **Required Data**                 | `division_id`, `name`, `description`                            |
| **Expected Response Data**        | Confirmation message on successful update                       |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' or 'referee' roles |

![Endpoint 12](/docs/endpoints/updated%20division.JPG)


| Aspect                            | Details                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| **Endpoint 13**                      | `/divisions/delete_division/<int:division_id>`                  |
| **HTTP Request Verb**             | DELETE                                                          |
| **Required Data**                 | `division_id`                                                   |
| **Expected Response Data**        | Message indicating successful deletion of the division          |
| **Authentication Methods**        | JWT required; Access limited to users with 'admin' role         |

![Endpoint 13](/docs/endpoints/delete%20division.JPG)



## R6 An ERD for the app

## R7 Detail any third-party servies your app will use
#### SQLAlchemy 

- 
#### Bcrypt 

- 
#### JwtManager

- 
#### 

## R8 Describe your projects model in terms of the relationships they have with each other

## R9 Discuss the database relations to be implemented

## R10 Describe the way tasks are allocated and tracked in your project


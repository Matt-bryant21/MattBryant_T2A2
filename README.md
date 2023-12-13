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

***Strong Community and Support:*** Being one of the oldest and most mature open-source relational databases, Postgres has a strong community and extensive documentation, ensuring reliable support.

### Conclusion
While SQLite is an excellent choice for simpler, embedded database needs, Postgres stands out for applications that demand higher performance, scalability, and a comprehensive set of features. Its ability to handle complex, enterprise-level applications with efficiency and reliability makes Postgres a preferred choice for many developers and organizations.

## R4 Identify and discuss the key functionalities and benefits of an ORM

## R5 Document all endpoints for your API
Endpoint documentation should include:
* HTTP request verb
* Required data where applicable 
* Expected response data 
* Authentication methods where applicable


## R6 An ERD for the app

## R7 Detail any third-party servies your app will use

## R8 Describe your projects model in terms of the relationships they have with each other

## R9 Discuss the database relations to be implemented

## R10 Describe the way tasks are allocated and tracked in your project

## References
https://www.boltic.io/blog/postgresql-vs-sqlite#:~:text=SQLite%20may%20be%20the%20better,data%20and%20support%20advanced%20features.

https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems
## Database selection for Group Project Agile

• We choose a relational database as it is better suited for structured data such as lists of users, blog posts, etc.,

• We use an ORM(Object Relational Mapper) here a flask extension called Flask-SQLAlchemy, which is a flask wrapper to SQLAlchemy as ORM makes it easier and more cost-effective to maintain the application over time because it automates object-to-table and table-to-object conversion and requires less code compared to embedded SQL and handwritten stored procedures. In many cases, it can improve the application's overall design.( https://www.theserverside.com/definition/object-relational-mapping-ORM)

• ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

• SQLALchemy uses Sqlite database for development and then at the time of deployment you can switch to MySQL or Postgres

• In Sqlite database is stored in a single file on disk

## Database Migrations, why do it?

(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

• Making updates to an existing database, as the application needs change or grow, is hard

• Because relational databases are centered around structured data

• When the structure changes the data that is already in the database needs to be “migrated” to the modified structure

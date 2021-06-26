from pony import orm

database = orm.Database()

class User(database.Entity):
    name = orm.Required(str)
    email = orm.Required(str)
    password = orm.Required(str)

database.bind(provider='sqlite', filename='inscription.db', create_db=True)
database.generate_mapping(create_tables=True)
# orm.set_sql_debug(True)

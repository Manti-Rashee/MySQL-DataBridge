import my_module as easy
from rich import print

# Dont use this it was for testing things that i changed that does they work or not

instance = easy.MySQLModule()
instance.connect_to_database('localhost','jano','qwert')
instance.connect_to_database('localhost','jano','qwert')
# print(instance.connection.is_connected())
# print(instance.is_database_exists('test'))
print(instance.create_database('janodb_balo'))
print(instance.delete_database('janodb_balo'))
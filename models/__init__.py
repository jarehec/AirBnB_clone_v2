from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()

storage = file_storage.FileStorage()
storage.reload()
"""CNC - dictionary = { Class Name (string) : Class Type }"""
CNC = file_storage.FileStorage.CNC

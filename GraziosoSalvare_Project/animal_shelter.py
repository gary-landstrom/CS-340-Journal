#python lib code
#Gary Landstrom

from pymongo import MongoClient
from bson.objectid import ObjectId



class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://localhost:42907')
        #initialize MongoClient, access to MongoDB databases
        #self.client = MongoClient('mongodb://%s:%s@localhost:42907/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        
    #method to implement c in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data is a dictionary
            return True
            
        else:
            raise Exception("Nothing to save: the data param is empty")
            
            
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} )
        
        return cursor
            
            
            
    def read(self, data):
        return self.database.animals.find_one(data) ##returns one item
    
    
    #Update animal information using animal ID as key value
    #FIXME: Revise for better implementation
    def update(self, data, age, animal, breed, color, DOB, datetime, monthyear, name, outcome, outcomesex, ageoutcome):
        if data is not None:
            self.database.animals.update_one(
                {"animal_id": data},
                {"$set": {
	"age_upon_outcome" : age,
	"animal_type" : animal,
	"breed" : breed,
	"color" : color,
	"date_of_birth" : DOB,
	"datetime" : datetime,
	"monthyear" : monthyear,
	"name" : name,
	"outcome_type" : outcome,
	"sex_upon_outcome" : outcomesex,
	"age_upon_outcome_in_weeks" : ageoutcome

}},
            )
                 
            return True
             #Will catch if the file fails to update    
        else:
            raise Exception("Could not update the file")
            
            
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_many(data)
            
            return True
        else:
            raise Exception("File was not deleted")
  
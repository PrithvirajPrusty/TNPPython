from pymongo import MongoClient
client = MongoClient()
dbname = client["samp"]
collection_name = dbname["student_details"]

class personal:
    def __init__(self):
        self.collage_name = "GIETU"
        self.year = 2024

class student(personal):
    def __init__(self,name,dept,*args,**kwargs):
        self.name = name
        self.dept = dept
        self.personal = vars(personal())
        self.args = args
        self.extras = kwargs
s1 = student("Prithviraj","Mechanical",countrycode="+91",phoneNumber=9337405893)
collection_name.insert_one(vars(s1))
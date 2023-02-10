from tinydb import TinyDB


db = TinyDB('db.json')



def get_tables():
    return db.tables()

def get_products(table_name: str) -> list[dict]:
    t = db.table(table_name)
    return t.all()
def get_phone(phone: str) -> list[dict]:
    t = db.table_class(phone)
    return t.all()

# class DB:
#     def __init__(self,path):
#         self.path = path
#         # Read the data from the file
#         self.data = {}
#         with open(self.path,'r') as f:
#             self.data = json.load(f)


#     def getPhone(self,brand,idx):
#         """
#         Return phone data by brand
#         args:
#             brand: str
#         return:
#             dict
#         """
#         phone = self.data[brand][idx]
#         data = {
#             'model':phone['name'],
#             'color':phone['color'],
#             'ram':phone['RAM'],
#             'price':phone['price'],
#             'memory':phone['memory'],
#             'image':phone['img_url'],
#         }
#         return data

#     def get_phone_list(self,brend):
#         """
#         Return phone list
#         """
#         phone = self.data[brend]
#         return list(phone.keys())

        

# # db = DB('db.json')
# # print(db.getPhone('Apple'))
# # print(db.get_phone_list('Apple'))



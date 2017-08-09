from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):

        store = StoreModel.find_by_name(name)

        if store:
            return store.json()

        return {'message': 'Store not found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' already exists".format(name)}, 404
        print('name', name)
        store = StoreModel(name)
        print('store', store)
        try:
            print('running save')
            store.save_to_db()
            print('save done')
        except:
            
            return {'message': 'An error occured while creating the store.'}, 500

        return store.json()

    def delete(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
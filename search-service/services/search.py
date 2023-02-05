from models.search import *
from typing import List

class SearchService():

    @staticmethod
    async def create(search_data):
        try:
            to_create = Search(**search_data)
            return await Search.insert_one(to_create)
        except Exception as e:  
            print("\nERROR => search controller => save_search : " + str(e))

    @staticmethod
    async def find_all_pag(index_pag):
        try:
            return await Search.find_all().sort(-Search.date).limit(10).skip(int(index_pag)-1).to_list()
        except Exception as e:
            print("\nERROR => search controller => save_search : " + str(e))

    @staticmethod
    async def update_status_by_id(id: str, status: str):
        try:
            return await Search.find_one(Search.id == id).update({"$set": {Search.status: status}})
        except Exception as e:
            print("\nERROR => update_status_by_id => save_search : " + str(e))


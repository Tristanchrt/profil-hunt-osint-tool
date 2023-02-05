from models.graph import Graph
from models.extractor import extractor
from typing import List

from controller.advanced import Advanced

class GraphController():

    @staticmethod
    async def create(graph_data) -> Graph:
        try:
            to_create = Graph(**graph_data)
            return await Graph.insert_one(to_create)
        except Exception as e:  
            print("ERROR => Graph controller => save_graph : " + str(e))

    @staticmethod
    async def find_all():
        try:
            data = await Graph.find_all().to_list()
            if not data:
                return []
            else:
                return data
        except Exception as e:
            print("ERROR => Graph controller => find_all_graph : " + str(e))

    @staticmethod
    async def find_one(id: str) -> Graph:
        # # Dev --
        # import os, json
        # path_dir = f'{os.getcwd()}/input'
        # for file in os.listdir(path_dir):
        #     if os.path.isfile(os.path.join(path_dir, file)):
        #         with open(os.path.join(path_dir, file), 'r') as f:
        #             data_in = json.load(f)
        #         curr_extract = extractor(data = data_in,
        #                                  name = file.strip('.json'),
        #                                  id_search = '1234')
        #         await extractor.insert_one(curr_extract)
        # # -------

        try:
            graph = await Graph.find_one(Graph.id_research == id)
            if graph:
                return graph
        except Exception as e:  
            print("ERROR => Graph controller => find_data_graph : " + str(e))
        
        try:
            data = await extractor.find(extractor.id_search == id).to_list()
            if len(data) is not 3:
                return "In progress"
        except Exception as e:  
            print("ERROR => Graph controller => find_data_extractors : " + str(e))
        
        try:   
            advanced = Advanced()
            data = advanced.run_advanced(data)
        except Exception as e:
            print("ERROR => Graph controller => Advanced: Data Lost : " + str(e))
    
        try:
            graph = Graph(data=data,
                        id_research=id)
            return await Graph.insert_one(graph)
        except Exception as e:  
            print("ERROR => Graph controller => save_graph : " + str(e))
        
        # Dev ---
        # try:
        #     await extractor.find_all(id_search='1234').delete()
        # except Exception as e:
        #     print("ERROR => Graph controller => delete_graph : " + str(e))
        # # -------
        
        # try:
        #     data = await Graph.find_one(Graph.id_research == id)
        #     return data
        # except Exception as e:
        #     print("ERROR => Graph controller => find_one_graph : " + str(e))

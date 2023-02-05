# from broker.producer import BK_PRODUCER
from models.extractor import Extractor
from controllers.basic import Basic
from config.config import initiate_database
from copy import deepcopy


class Transform:   
    
    async def send_data(self, data, topic_name):
        try:
            await initiate_database()
        except Exception as e:
            print(f'[{topic_name}] database initiation: {e}')
        
        return await self.run_processing(data, topic_name)
    
    async def run_processing(self, data, topic_name):
        data_from_broker = deepcopy(data)
        id_search = data_from_broker['search_id']
        data_to_process = data_from_broker['data']
    
        basic_process = Basic(topic_name)
        data_to_process = basic_process.run_format_revision(data_to_process)

        # data = basic_process.run_identification(data)
        # data = basic_process.run_keyword_classification(data)
        
        try:
            if data_to_process is not None:
                to_create = Extractor(
                    name=topic_name,
                    id_search=id_search,
                    data=data_to_process
                )
                data_saved =  await Extractor.insert_one(to_create)
                data_from_broker['data'] = data_saved.data
                return data_from_broker
            else:
                raise Exception('Data Lost')     
        except Exception as e:
            print(f'[{topic_name}] writing db error: {e}')


    async def find_all_data(self):
        try:
            return await Extractor.find_all().to_list()
        except:
            print('Error finding all data transform')
            return None
        


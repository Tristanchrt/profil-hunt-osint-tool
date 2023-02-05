from services.recap import Recapitulation
from services.bypass import Bypass
from services.compound import Compounder
from services.filter import Filter


class Advanced:
    
    def run_advanced(self, data):
        try:
            res = data
            while res != None:
                res = self.__run_recapitulation(data)
                res = self.__run_bypass(data, res)
                # res = self.__run_compounder(data, res)
                
                res = self.__run_filter(res)
                return res
            raise Exception
        except Exception as e:
            print(f'Advanced failed: {e}')
            return res
            
    def __run_recapitulation(self, data):
        try:
            recapitulation = Recapitulation(data)
            return recapitulation.run_recapitulation()
        except Exception as e:
            print(f'Recapitulation failed: {e}')

    def __run_bypass(self, data, res):
        try:
            bypass = Bypass(data)
            return bypass.run_bypass(res)
        except Exception as e:
            print(f'Bypass failed: {e}')
            
    def __run_compounder(self, data, res):
        try:
            compounder = Compounder(data)
            return compounder.run_compounder(res)
        except Exception as e:
            print(f'Compounder failed: {e}')

    def __run_filter(self, res):
        try:
            filter = Filter()
            return filter.run_filter(res)
        except Exception as e:
            print(f'Filter failed: {e}')
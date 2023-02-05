from math import cos, sin
import random
from itertools import groupby

class Filter():

    def run_filter(self, res):
        for relation in res.get('nodes'):
            if relation.get('id') != '0' and relation.get('score') == 0:
                res.get('nodes').remove(relation)
            self.get_coord_graph(relation)
            
        res.update({"nodes": [x for x in res.get('nodes') if res.get('nodes').count(x) == 1]})
        # res.update({"nodes": sorted(res.get('nodes'), key=lambda x: x['score'], reverse=True)})
        return res
    
    def get_coord_graph(self, relation):
        x_center = 0
        y_center = 0
        if relation.get('id') == 0:
            relation.update({"xOffset": x_center})
            relation.update({"yOffset": y_center})
        else:
            distance = relation.get('score') * 1000
            angle = random.randint(0, 360)
            relation.update({"xOffset": distance * cos(angle) + x_center})
            relation.update({"yOffset": distance * sin(angle) + x_center})
class Recapitulation():

    def __init__(self, data):
        for document in data:
            match document.name:
                case 'LINKEDIN':
                    self.linkedin_data = document.data
                case 'INSTA':
                    self.insta_data = document.data
                case 'FACEBOOK':
                    self.facebook_data = document.data

    def run_recapitulation(self):
        id = 0
        lst_names = []
        nodes = []
        edges = []
        nodes.append(self.build_root(id))
        
        if self.linkedin_data:
            for relation in self.linkedin_data.get('relations'):
                node = {}
                id += 1
                node.update({"id": str(id)})
                name = ' '.join(relation.get('names'))
                node.update({"name": name})
                lst_names.append(name.lower())
                node.update({"job_description": relation.get('job_description')})
                node.update({"city": relation.get('city')})
                node.update({"country": relation.get('country')})
                node.update({"state": relation.get('state')})
                node.update({"linkedin_relation": True})
                nodes.append(node)
        

        if self.insta_data:
            for relation in self.insta_data.get('relations'):
                if relation.get('full_name') is not None:
                    if relation.get('full_name').lower() in lst_names:
                        for curr_node in nodes:
                            if curr_node.get('name').lower() == relation.get('full_name').lower():
                                node = curr_node  
                    elif relation.get('full_name').lower() not in lst_names:
                        node = {}
                        id += 1
                        node.update({"id": str(id)})
                        node.update({"name": relation.get('full_name')})
                        lst_names.append(relation.get('full_name').lower())
                else:
                    node = {}
                    id += 1
                    node.update({"id": str(id)})
                    
                node.update({"insta_username": relation.get('username')})
                node.update({"pic_url": relation.get('pic_url')})
                node.update({"insta_follower": relation.get('insta_follower')})
                node.update({"insta_following": relation.get('insta_following')})
                nodes.append(node)
        
        if self.facebook_data:
            for relation in self.facebook_data.get('relations'):
                if relation.get('name') is not None:
                    if relation.get('name').lower() not in lst_names:
                        node = {}
                        id += 1
                        node.update({"id": str(id)})
                        lst_names.append(relation.get('name').lower())
                    else:
                        for curr_node in nodes:
                            if curr_node.get('name') and curr_node.get('name').lower() == relation.get('name').lower():
                                node = curr_node

                    node.update({"name": relation.get('name')})
                    node.update({"pic_url": relation.get('pic_url')})
                    node.update({"fb_relation": True})
                    nodes.append(node)
        
        return {"nodes": nodes, "edges": edges}
            
            
    def build_root(self, id):
        node = {}
        node.update({"id": str(id)})
        
        if self.linkedin_data:
            for key, val in self.linkedin_data.get('profile')[0].items():
                if key != 'company' and val is not None:
                    node.update({key: str(val)})
            if self.linkedin_data.get('experience')[0]:
                node.update({"job": self.linkedin_data.get('experience')[0].get('job')})
                node.update({"company": self.linkedin_data.get('experience')[0].get('company')})  
                node.update({"area_info": self.linkedin_data.get('experience')[0].get('area_info')})  
            if self.linkedin_data.get('education')[0]:
                node.update({"school": self.linkedin_data.get('education')[0].get('school')})    
        
        if self.insta_data:
            for key, val in self.insta_data.get('profile').items():
                 if val is not None:
                    node.update({key: str(val)})
        
        if self.facebook_data:
            for key, val in self.facebook_data.get('profile').items():
                if val is not None and val != []:
                    node.update({key: val})
                                    
        return node
            


class Compounder():
    
    def __init__(self, data):        
        for document in data:
            match document.name:
                case 'LINKEDIN':
                    self.linkedin_data = document.data
                case 'INSTA':
                    self.insta_data = document.data
                case 'FACEBOOK':
                    self.facebook_data = document.data
                    
    def run_compounder(self, res):
        compound = {}
        tmp_fb = []
        tmp_follower = []
        tmp_following = []
        tmp_linkedin = []
        
        for relation in res.get('nodes'):
            if relation.get('fb_relation'):
                tmp_fb.append(str(relation.get('id')))
            if relation.get('insta_follower'):
                tmp_follower.append(str(relation.get('id')))
            if relation.get('insta_following'):
                tmp_following.append(str(relation.get('id')))
            if relation.get('linkedin_relation'):
                tmp_linkedin.append(str(relation.get('id')))
                
        compound.update({"Facebook Relations": tmp_fb})
        compound.update({"Instagram Follower Relations": tmp_follower})
        compound.update({"Instagram Following Relations": tmp_following})
        compound.update({"LinkedIn Relations": tmp_linkedin})
        
        res.update({"compound": compound})
        
        return res
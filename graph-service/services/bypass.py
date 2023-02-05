import openai
import translators as ts
# from googletrans import Translator
# from google.cloud import translate_v2 as translate

class Bypass():

    def __init__(self, data):        
        for document in data:
            match document.name:
                case 'LINKEDIN':
                    self.linkedin_data = document.data
                case 'INSTA':
                    self.insta_data = document.data
                case 'FACEBOOK':
                    self.facebook_data = document.data
                    
        self.coef_city = 3
        self.coef_job = 6
        self.coef_relation = 5
    
    def set_globals(self, res):
        self.nb_relation = len(res.get('nodes')) - 1
        self.nb_picture = len(self.facebook_data.get('medias')) + len(self.insta_data.get('medias')) 

    def run_bypass(self, res):
        self.set_globals(res)
        
        if self.facebook_data:
            try:
                res.get('nodes')[0].update({"description": self.get_description()})
            except:
                pass
        
        profile = res.get('nodes')[0]
        for relation in res.get('nodes'):
            if relation.get('name') is not None:
                relation.update({"score": self.get_score(relation, profile)})        
        return res
    
    def complete_text(prompt, model, temperature=0.5):
        try:
            openai.organization = "org-D8qp722VQnXSOwgAEdG6tqYR"
            openai.api_key = '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'
            completions = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=64,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                temperature=temperature
            )
        except Exception as e:
            print(e)
            return None
        message = completions.choices[0].text
        return message.strip()
    
    def get_description(self):
        to_prompt = 'Say that is a test'
        """for about in self.facebook_data.get('profile'):
            try:
                result = translator.translate(self.facebook_data.get('profile').get(about), src='fr', dest='en')
                print(result.text)
                to_prompt += ', '.join(result.text) + '. '
            except Exception as e:
                print(e)"""
        
        try:
            to_prompt =  ts.translate_text("Bonjour")
        except Exception as e:
            print('Fail Translate: ', e)
        
        try:
            model = "text-davinci-003"
            print(to_prompt)
            description = self.complete_text(to_prompt, model)
            print('Description:', description)
            return description
        except Exception as e:
            print(e)
            return None
            
    def get_score(self, relation, profile):
        score = 0
        coef_tot = 0
        
        if relation.get('city') is not None:
            if relation.get('city') in profile.get('area_info'):
                score += 2 * self.coef_city
        coef_tot += self.coef_city
        
        if relation.get('job_description') is not None:
            for word in relation.get('job_description').split(' '):
                if word in profile.get('company'):
                    score += 3 * self.coef_job
                    break
        coef_tot += self.coef_job
                
        if relation.get('fb_relation') is not None:
            score += 2 * self.coef_relation * relation.get('fb_relation')
        coef_tot += 2 * self.coef_relation

        if relation.get('insta_follower') is not None:
            score += 3 * self.coef_relation * relation.get('insta_follower')
        coef_tot += 3 * self.coef_relation
        
        if relation.get('insta_following') is not None:
            score += 4 * self.coef_relation * relation.get('insta_following')
        coef_tot += 4 * self.coef_relation
        
        if relation.get('linkedin_relation') is not None:
            score += 3 * self.coef_relation * relation.get('linkedin_relation')
        coef_tot += 3 * self.coef_relation
        
        try:
            score = score / coef_tot
            if score > 1:
                score = 1
            return score
        except ZeroDivisionError:
            return 0
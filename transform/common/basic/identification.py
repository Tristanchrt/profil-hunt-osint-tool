from common.basic.utils import url_to_img

class Identification():
    
    def __init__(self, data, topic_name):
        self.payload = data
        self.topic_name = topic_name
    
    # Analyse every media and class by recognition
    # Associate identities
    def run_identification(self):
        match self.topic_name:
            case 'LINKEDIN':
                return self.run_linkedin_identification()
            case 'INSTA':
                return self.run_insta_identification()
            case 'FACEBOOK':
                return self.run_facebook_identification()                    
            case _:
                print('[Identification]Topic_name unknow:', self.topic_name)
                return None
    
    def run_linkedin_identification(self):
        # image = face_recognition.load_image_file()
        
        # Find all the faces in the image
        # face_locations = face_recognition.face_locations(image)

        # Or maybe find the facial features in the image
        # face_landmarks_list = face_recognition.face_landmarks(image)

        # Or you could get face encodings for each face in the image:
        # list_of_face_encodings = face_recognition.face_encodings(image)
        return None
    
    def run_insta_identification(self):
        return None
        try:
            from deepface import DeepFace

            models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace",
                      "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]

            for media in self.payload.get('medias'):
                for follower in self.payload.get('relations'):

                    img_follower = url_to_img(follower.get('pic_url'))
                    media_follower = url_to_img(media.get('img_url'))
                    
                    result = DeepFace.verify(
                        img1_path=media_follower, img2_path=img_follower, model_name=models[1])
                    if result:
                        print('\nRESULT DEEPFACE =>', result)

                    return None

        except Exception as e:
            print('Error', e)
    
    def run_facebook_identification(self):
        return None
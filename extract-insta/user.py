class User:
    def __init__(self, username, cl):
        self.connection = cl
        self.username = username
        self.id = self.connection.user_id_from_username(self.username)
        self.description = self.connection.user_info_by_username(self.username)
        self.followers = self.connection.user_followers(self.id)
        self.following = self.connection.user_following(self.id)
        self.medias = self.connection.user_medias(self.id)

    def get_userid(self):
        return self.id

    def get_username(self):
        return self.username

    def get_description(self):
        return self.description

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_medias(self):
        return self.medias

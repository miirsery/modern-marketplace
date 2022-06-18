class UserWorker:

    def user_delete_avatar(self, user, default_avatar):
        user.avatar.delete(save=False)
        user.avatar = default_avatar
        return user

#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5


class BaseReseponse(object):
    def __init__(self):
        self.status = False
        self.data=None
        self.msg=None

    def get_dict(self):
        return self.__dict__



class LikeReseponse(BaseReseponse):
    def __init__(self):
        self.code = 0
        super(LikeReseponse,self).__init__()


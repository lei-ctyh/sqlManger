class ContainerUtil(object):
    app = None
    manger = None



    @staticmethod
    def get_manger_self():
        return ContainerUtil.manger

    @staticmethod
    def set_manger_self(self):
        ContainerUtil.manger = self

    @staticmethod
    def get_app_self():
        return ContainerUtil.app

    @staticmethod
    def set_app_self(self):
        ContainerUtil.app = self

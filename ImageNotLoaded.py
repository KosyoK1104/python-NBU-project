class ImageNotLoadedException(RuntimeWarning):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def image_not_loaded(class_name):
        return ImageNotLoadedException('The image of ' + class_name + ' couldn\'t be loaded')

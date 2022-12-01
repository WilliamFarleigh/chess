class Util:
    def is_right_type(object, type_of_object):
        if (type(object) == type_of_object):
            return True
        raise Exception(str(object) + " is not an instance of " + type_of_object)
Util.is_right_type = staticmethod(Util.is_right_type)
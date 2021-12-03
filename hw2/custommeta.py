class CustomMeta(type):
    def __new__(cls, clsname, superclasses, attribute_dict):
        new_attribute_dict = {}
        for attribute_key, attribute_val in attribute_dict.items():
            if not (attribute_key.startswith('__') and attribute_key.endswith('__')):
                attribute_key = 'custom_' + attribute_key
            new_attribute_dict[attribute_key] = attribute_val
        return super().__new__(cls, clsname, superclasses, new_attribute_dict)

    def __call__(cls, *args, **kwargs):
        new_attribute_dict = {}

        new_object = super().__call__(*args, **kwargs)

        for attribute_key, attribute_val in new_object.__dict__.items():
            if not (attribute_key.startswith('__') and attribute_key.endswith('__')):
                attribute_key = 'custom_' + attribute_key
            new_attribute_dict[attribute_key] = attribute_val

        new_object.__dict__ = new_attribute_dict

        return new_object

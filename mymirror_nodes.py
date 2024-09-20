import json

class JsonFromString:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING",)
            },
        }

    RETURN_TYPES = ("JSON",)
    RETURN_NAMES = ("JSON",)

    FUNCTION = "do_work"

    CATEGORY = "MyMirror/Json"

    def do_work(self, string):
        return (json.loads(string), )

class JsonListFromStrings:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "str_1": ("STRING", {"forceInput": True}),
                "str_2": ("STRING", {"forceInput": True}),
                "str_3": ("STRING", {"forceInput": True}),
                "str_4": ("STRING", {"forceInput": True}),
                "str_5": ("STRING", {"forceInput": True}),
                "str_6": ("STRING", {"forceInput": True}),
                "str_7": ("STRING", {"forceInput": True}),
                "str_8": ("STRING", {"forceInput": True})
            },
        }

    RETURN_TYPES = ("JSON",)
    RETURN_NAMES = ("JSON",)

    FUNCTION = "do_work"

    CATEGORY = "MyMirror/Json"

    def do_work(self, str_1=None, str_2=None, str_3=None, str_4=None, str_5=None, str_6=None, str_7=None, str_8=None):    
        strings = []
        def add_item(item):
            nonlocal strings
            if not item is None and len(item) > 0:
                strings += [ item ]
        add_item(str_1)
        add_item(str_2)
        add_item(str_3)
        add_item(str_4)
        add_item(str_5)
        add_item(str_6)
        add_item(str_7)
        add_item(str_8)
        return (strings, )


class JsonListContainsAny:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list_a": ("JSON", {"forceInput": True}),
                "list_b": ("JSON", {"forceInput": True})
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

    FUNCTION = "test"

    CATEGORY = "MyMirror/Json"

    def test(self, list_a, list_b):
        for e in list_a:
            if e in list_b:
                return (True,)
        return (False,)

class JsonListContainsAll:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list_a": ("JSON", {"forceInput": True}),
                "list_b": ("JSON", {"forceInput": True})
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

    FUNCTION = "test"

    CATEGORY = "MyMirror/Json"

    def test(self, list_a, list_b):
        for e in list_a:
            if not e in list_b:
                return (False,)
        return (True,)


class ClothCues:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")

    RETURN_NAMES = ("short-sleeves", "long-sleeves", "elbow-length-sleeves")

    FUNCTION = "test"

    CATEGORY = "MyMirror/Json"

    def test(self):
        return ("short-sleeves", "long-sleeves", "elbow-length-sleeves")



NODE_CLASS_MAPPINGS = {
    'JsonFromString': JsonFromString,
    'JsonListFromStrings': JsonListFromStrings,

    'ClothCues': ClothCues,

    'JsonListContainsAny': JsonListContainsAny,
    'JsonListContainsAll': JsonListContainsAll
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'JsonFromString': 'Json From String',
    'JsonListFromStrings': 'Json List From Strings',

    'ClothCues': 'ClothCues',

    'JsonListContainsAny': 'List Contains Any',
    'JsonListContainsAll': 'List Contains All'
}
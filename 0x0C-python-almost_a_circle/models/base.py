"""Module Class Base"""
import json
import os
import csv


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init variables of Objects Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        if list_objs is None or len(list_objs) == 0:
            obj_list = []
        else:
            obj_list = []
            for element in list_objs:
                obj_list.append(element.to_dictionary())

        json_str = Base.to_json_string(obj_list)

        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return a list of a JSON representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attr sets"""
        dummy_instance = None

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1, 1, 1)

        if cls.__name__ == "Square":
            dummy_instance = cls(1)

        if dummy_instance is not None:
            dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """laod a JSON file"""
        ins_list = []
        f_name = "{}.json".format(cls.__name__)

        if os.path.isfile(f_name):
            with open(f_name) as f:
                obj = cls.from_json_string(f.read())
                for dict_obj in obj:
                    ins_list.append(cls.create(**dict_obj))
                return ins_list
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to CSV"""
        if cls.__name__ == "Rectangle":
            names = ["id", "width", "height", 'x', 'y']
        else:
            names = ["id", "size", 'x', 'y']
        with open("{}.csv".format(cls.__name__), 'w') as f:
            if list_objs is not None:
                w_csv = csv.DictWriter(f, names)
                w_csv.writeheader()
                w_csv.writerows([obj.to_dictionary() for obj in list_objs])
            else:
                w_csv = csv.writer(f)
                w_csv.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes to CSV"""
        try:
            with open("{}.csv".format(cls.__name__), newline='') as f:
                r_csv = csv.DictReader(f)
                n_list = []
                for line in r_csv:
                    for key, value in line.items():
                        line[key] = int(value)
                    n_list.append(line)
                return [cls.create(**obj) for obj in n_list]
        except Exception:
            return []

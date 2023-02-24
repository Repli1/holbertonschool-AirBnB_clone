
#!/usr/bin/python3
""""""
import json
import os.path


class FileStorage:
    """"""
    __file_path = "savefile.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects.append(obj, obj.id)
    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            write_data = f.write(json.dumps(FileStorage.__objects))
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                read_data = f.read()
            return json.loads(read_data)

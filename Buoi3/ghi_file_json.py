import json
khach_hang = { 
    "MaKH": "122",
    "HoTen": "nguyen Van A",
}

data_file = open("du_lieu/khach_hang.json", "w")
json.dump(khach_hang, data_file, indent=4)
data_file.close()
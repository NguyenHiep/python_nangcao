import json

data_file = open("du_lieu/khach_hang.json", encoding="utf-8")
noi_dung = json.load(data_file) # Load noi dung file len

# Thong tin bo sung
bo_sung = {
    "Dia chi" : "Nguyen chi thanh",
    "So DT" : "01222145789654"
}

# Cap nhat la data
noi_dung.update(bo_sung)

# Ghi de noi dung moi len noi dung cu
data_file = open("du_lieu/khach_hang.json", "w")
json.dump(noi_dung, data_file, indent=4)
data_file.close()
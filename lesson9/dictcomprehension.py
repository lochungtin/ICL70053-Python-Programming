ids = {"Luca": "20013", "Josiah": "10027", "Rob": "10112", "Harry": "20064"}
names = {v: k for (k, v) in ids.items() if v.startswith("2")}
assert names == {"20013": "Luca", "20064": "Harry"}

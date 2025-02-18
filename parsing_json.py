import json
with open("sample-data.json", "r") as openfile:
    data = json.load(openfile)

s = """Interface Status
============================================================================================
DN                                              Description                    Speed     MTU
---------------------------------------------- -----------------------------  -------  ------
"""
for el in data["imdata"]:
    s+=el["l1PhysIf"]["attributes"]["dn"]
    s+="\n"
print(s)

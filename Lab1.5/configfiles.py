import glob

result = {}


#создаем словарь привязки ip к файлам

for fname in glob.glob("config_files\*.txt"):
    for line in open(fname):
        if line.strip().lower().startswith("ip address"):
            if fname in result.keys():
                result[fname].append(line.strip().replace("ip address",""))
            else:
                result[fname] = [line.strip().replace("ip address", "")]

#чистим получившиеся списки от повторов

for key in result.keys():
    result[key] = list(set(result[key]))

print(result)
def listToFile(path, data_list):
    with open(path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + '\n')
        
lst = ["example", "storage"]
listToFile(r"C:\projects\PP2_RZ\Lab6\Storage.txt", lst)

       
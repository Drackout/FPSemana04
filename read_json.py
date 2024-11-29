import json

#"data.json"
fileName = input()


try:
    with open(fileName, 'rt', encoding='utf-8') as file:
        data = json.load(file)

    print(data)
except:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")

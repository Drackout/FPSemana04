import json

#"data.json"
fileName = input()


try:
    with open(fileName, 'rt', encoding='utf-8') as file:
        data = json.load(file)

    print("caminho_certo/data.json")
    print(data)
except:
    print("caminho_errado/data.json")
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")
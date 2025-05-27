import json

def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            tarefas = json.load(f)
            print("DEBUG: Conteúdo do arquivo JSON carregado:")
            print(json.dumps(tarefas, indent=4, ensure_ascii=False))
        #print(f"DEBUG: {len(tarefas)} tarefas carregadas.")
    except FileNotFoundError:
        tarefas = [] 
    except json.JSONDecodeError:
        print("⚠️ Erro ao carregar JSON. Arquivo corrompido.")
        tarefas = []
       
def salvar_tarefas():
    global tarefas
    with open("tarefas.json", "w", encoding="utf-8") as f: 
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def adicionar_tarefa():
    global tarefas
    nome = input("Digite o nome da tarefa: ")
    prioridade = input("Digite a prioridade (baixa, media, alta): ").lower()

    if prioridade not in ["baixa", "media", "alta"]:
        print("Prioridade invalida. Use: baixa, media ou alta.")
        return
    
    tarefa = {"nome": nome, "prioridade": prioridade, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas()
    print("Tarefa adicionada com sucesso!")
    input("🔄 Enter para continuar...")

def listar_tarefas():
    global tarefas 

    if not tarefas:
        print("Nenhuma tarefa cadastrada.") 
        print(">>> Saindo da função listar_tarefas() - lista vazia")
        return
    
    print("\n---Lista de Tarefas ---")
    for i, t in enumerate(tarefas):
        status = " ✅ " if t["concluida"] else " ❌ "
        print(f"{i + 1}. {t['nome']} (prioridade: {t['prioridade']}) - {status}")

    print(">>> Saindo da função listar_tarefas() - fim")

def listar_prioridade_alta():
    global tarefas
    tarefas_alta = [t for t in tarefas if t["prioridade"] == "alta"]
    if not tarefas_alta:
        print("Nenhuma tarefa com prioridade alta.")
    else:
        print("\nEstas são as tarefas com PRIORIDADE ALTA:")
        for i, tarefa in enumerate(tarefas_alta, start=1):
            print(f"{i}. {tarefa['nome']}")

def concluir_tarefa():
    listar_tarefas()
    global tarefas
    try:
        indice = int(input("\nDigite o numero da tarefa a concluir: ")) -1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas()
            print("Tarefa marcada como concluida!")
        else: print("Número invalido.")
    except ValueError:
        print("Entrada invalida. Digite um número.")

def deletar_tarefa():
    global tarefas
    listar_tarefas()
    if not tarefas:
        return
    try:
        indice = int(input("\nDigite o numero da tarefa a deletar: ")) -1
        if 0 <= indice <len(tarefas):
            tarefas_removida = tarefas.pop(indice)
            salvar_tarefas()
            print(f"🗑️  Tarefa '{tarefas_removida['nome']}' \n Deletada com sucesso!")
        else: 
            print("Número invalido.")
    except ValueError:
        print("Digite um numero.")

   ### Menu Principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. mostrar tarefa como concluida ")
        print("4. Listar tarefas de prioridade alta")
        print("5. Deletar uma tarefa")
        print("6. Sair")

        opcao =input("Escolher uma opção: ") # Controle  

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            listar_prioridade_alta()
        elif opcao == "5":
            deletar_tarefa()
        elif opcao == "6":
            print("👋Encerrando o programa.")
            break
        else: 
            print("Opção invalida.")
carregar_tarefas()
menu()
            



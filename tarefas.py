tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    prioridade = input("Digite a prioridade (baixa, media, alta): ").lower()
    tarefa = {"nome": nome, "prioridade": prioridade, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa['nome']} - prioridade: {tarefa['prioridade']}")

def listar_prioridade_alta():
    tarefas_alta = [t for t in tarefas if t["prioridade"] == "alta"]
    if not tarefas_alta:
        print("Nenhuma tarefa com prioridade alta.")
    else:
        print("Estas tarefas é de prioridade ALTA:")
        for i, tarefa in enumerate(tarefas_alta, start=1):
            print(f"{i}. {tarefa['nome']}")

### Menu Principal
while True:
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Listar tarefas de prioridade ALTA")
    print("4. Sair")

    opcao =input("Escolher uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_prioridade_alta()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else: 
        print("Opção invalida . Tente noavamente.")
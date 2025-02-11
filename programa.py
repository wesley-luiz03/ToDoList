tarefas = []

def main():
    while True:
        print("\n--- Lista de Tarefas ---")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefa")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção Inválida! Tente novamente. ")
            
def adicionar_tarefas():
    tarefa=input("Digite a nova tarefa: ")
    tafefas.append(tarefa)
    print("Tarefas adicionada com sucesso!")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")
        for i, tarefas in enumerate(tarefa, 1)
            print(f"{i}. {tarefa}")

def remover_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida!")
            else:
                print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

if_name_=="_main_":
    main()
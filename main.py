from Estruturas import Fila, Pilha

fila_vacinacao = Fila()
pilha_frascos = Pilha()
vacinados_lista = [] # lista vazia para os ja vacinados

Max_Pessoas = 15
doses_no_frasco_atual = 0
total_doses_disponiveis = 15
pessoas_na_fila = 0

# empilhando os 3 frascos com 5 doses cada
for i in range(3, 0, -1):
    pilha_frascos.empilhar(5) 

def menu():
    global doses_no_frasco_atual, total_doses_disponiveis, pessoas_na_fila
    
    while True:
        print("\n--- SISTEMA DE VACINACAO ---")
        print("1 - Adicionar pessoa na fila")
        print("2 - Imprimir pessoas da fila")
        print("3 - Imprimir doses disponiveis")
        print("4 - Vacinar uma pessoa")
        print("5 - Exibir total de pessoas vacinadas")
        print("0 - Sair")
        print("--------------------------------------")
        
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            if (len(vacinados_lista) + pessoas_na_fila) < Max_Pessoas:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                fila_vacinacao.enfileirar({"nome": nome, "cpf": cpf})
                pessoas_na_fila += 1
                print("Pessoa adicionada com sucesso!")
            else:
                print("Limite diário de 15 pessoas atingido.")

        elif opcao == "2":
            fila_vacinacao.imprimeFila()

        elif opcao == "3":
            print(f"Total de doses restantes no estoque: {total_doses_disponiveis}")

        elif opcao == "4":
            if total_doses_disponiveis > 0:
                pessoa = fila_vacinacao.desenfileirar()
                if pessoa:
                    # lógica do frasco, se não tem dose no uso, desempilha
                    if doses_no_frasco_atual == 0:
                        doses_no_frasco_atual = pilha_frascos.desempilhar()
                    
                    doses_no_frasco_atual -= 1
                    total_doses_disponiveis -= 1
                    pessoas_na_fila -= 1
                    vacinados_lista.append(pessoa['nome'])
                    
                    print(f"Vacinado: {pessoa['nome']} (CPF: {pessoa['cpf']})")
                    print(f"Dose aplicada! Restam {doses_no_frasco_atual} doses neste frasco.")
                else:
                    print("Não há ninguém na fila!")
            else:
                print("Acabaram as vacinas por hoje!")

        elif opcao == "5":
            print(f"Total de pessoas vacinadas até agora: {len(vacinados_lista)}")
            if vacinados_lista:
                print("Nomes dos vacinados:")
                for nome in vacinados_lista:
                    print(f"- {nome}")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

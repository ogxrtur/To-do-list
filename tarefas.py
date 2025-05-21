import json
import os

ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)

def mostrar_tarefas(tarefas):
    print("\n📝 Suas tarefas:")
    if not tarefas:
        print("   📭 Nada por aqui. Que tal adicionar algo?")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "✅" if tarefa['concluida'] else "❌"
            print(f"   {i + 1}. {status} {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    desc = input("🔹 O que você quer adicionar à lista? ").strip()
    if desc:
        tarefas.append({'descricao': desc, 'concluida': False})
        salvar_tarefas(tarefas)
        print(f"✅ Tarefa \"{desc}\" adicionada com sucesso!")
    else:
        print("⚠️ Tarefa vazia não vale, hein!")

def concluir_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            i = int(input("✅ Qual tarefa você concluiu? (número) ")) - 1
            if 0 <= i < len(tarefas):
                tarefas[i]['concluida'] = True
                salvar_tarefas(tarefas)
                print(f"🎉 Tarefa \"{tarefas[i]['descricao']}\" marcada como concluída!")
            else:
                print("⚠️ Número fora da lista.")
        except:
            print("⚠️ Digite um número válido.")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            i = int(input("🗑️ Qual tarefa deseja remover? (número) ")) - 1
            if 0 <= i < len(tarefas):
                removida = tarefas.pop(i)
                salvar_tarefas(tarefas)
                print(f"🧹 Tarefa \"{removida['descricao']}\" foi removida.")
            else:
                print("⚠️ Número fora da lista.")
        except:
            print("⚠️ Digite um número válido.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n📋 Menu de Tarefas")
        print("1️⃣ Ver tarefas")
        print("2️⃣ Adicionar nova tarefa")
        print("3️⃣ Marcar tarefa como concluída")
        print("4️⃣ Remover uma tarefa")
        print("5️⃣ Sair")
        escolha = input("👉 Escolha uma opção (1-5): ")

        if escolha == '1':
            mostrar_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefa(tarefas)
        elif escolha == '3':
            concluir_tarefa(tarefas)
        elif escolha == '4':
            remover_tarefa(tarefas)
        elif escolha == '5':
            print("👋 Até logo! Volte sempre para manter sua vida em ordem!")
            break
        else:
            print("❗ Ops! Escolha uma opção válida (1 a 5).")

if __name__ == "__main__":
    print("🎯 Bem-vindo ao seu Gerenciador de Tarefas!")
    menu()
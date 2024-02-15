import random

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        return "Usuário vence!"
    else:
        return "Computador vence!"

opcoes = ['pedra', 'papel', 'tesoura']

while True:
    escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para terminar o jogo): ").lower()
    
    if escolha_usuario == 'sair':
        print("O jogo foi encerrado.")
        break
    elif escolha_usuario not in opcoes:
        print("Opção inválida. Por favor, escolha entre pedra, papel ou tesoura.")
        continue
    
    escolha_computador = random.choice(opcoes)
    
    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")
    
    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    print(resultado)
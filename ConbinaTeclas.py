import keyboard
import time

# Lista para armazenar as combinações de teclas e intervalos de tempo
combinacoes = []

# Solicitar ao usuário para inserir combinações de teclas e intervalos de tempo
while True:
    teclas_desejadas = input("Digite as teclas desejadas (ou 'exit' para encerrar): ")
    
    if teclas_desejadas.lower() == 'exit':
        break

    intervalo_de_tempo = int(input("Digite o intervalo de tempo em segundos: "))

    # Adicionar a combinação à lista
    combinacoes.append((teclas_desejadas, intervalo_de_tempo))

# Função para enviar uma combinação de teclas
def enviar_combinacao_teclas(teclas):
    keyboard.press_and_release(teclas)
    print(f"Combinação de teclas {teclas} enviada!")

# Loop principal
for teclas, intervalo in combinacoes:
    # Envia a combinação de teclas
    enviar_combinacao_teclas(teclas)

    # Aguarda o intervalo de tempo definido pelo usuário
    time.sleep(intervalo)

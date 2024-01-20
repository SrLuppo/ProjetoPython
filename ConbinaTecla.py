import keyboard
import time

# Configuração do intervalo de tempo em segundos
# intervalo_de_tempo = 60  # por exemplo, 60 segundos (1 minuto)

# Solicitar ao usuário para inserir o intervalo de tempo em segundos
intervalo_de_tempo = int(input("Digite o intervalo de tempo em segundos: "))


# Função para enviar a combinação de teclas
def enviar_combinacao_teclas():
    keyboard.press_and_release('ctrl+q')
    print("Combinação de teclas enviada!")

# Loop principal
while True:
    # Envia a combinação de teclas
    enviar_combinacao_teclas()

    # Aguarda o intervalo de tempo
    time.sleep(intervalo_de_tempo)

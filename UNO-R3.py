import time

# Definindo o estado inicial dos pinos de entrada e saída como False (desligados)

entrada = False  
saida = False   

# Função para simular a mudança de estado do pino de entrada
def mudar_estado_entrada():
    global entrada
    entrada = not entrada  

# Função para simular a mudança de estado do pino de saída
def mudar_estado_saida():
    global saida
    saida = not saida  
    if saida:
        print("Pino de saída ativado!")
    else:
        print("Pino de saída desativado!")

# Vamos Testar
try:
    while True:
        # Simulando a mudança de estado do pino de saída a cada 2 segundos
        mudar_estado_saida()
        time.sleep(2)

        # Simulando a detecção da mudança de estado do pino de entrada
        mudar_estado_entrada()
        print("Estado do pino de entrada mudou para:", entrada)

except KeyboardInterrupt:
    print("\nTeste interrompido pelo usuário.")

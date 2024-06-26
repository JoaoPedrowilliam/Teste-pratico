
# Teste pratico Psyche Aerospace 🚀🚀

Este código em Python simula a interação entre pinos de entrada e saída, utilizando variáveis booleanas para representar o estado desses pinos. Aqui está uma visão geral do que cada parte do código faz


### Inicialização dos Estados
 As variáveis entrada e saida são inicializadas como False, representando o estado inicial dos pinos de entrada e saída, respectivamente.

### Função para Mudar o Estado da Entrada
A função mudar_estado_entrada() é definida para simular a mudança de estado do pino de entrada. Ela inverte o valor da variável entrada sempre que é chamada.

### Função para Mudar o Estado da Saída
 A função mudar_estado_saida() é definida para simular a mudança de estado do pino de saída. Além de inverter o valor da variável saida, ela também imprime uma mensagem indicando se o pino de saída foi ativado ou desativado.

### Loop Principal
Um loop infinito while True é iniciado para simular o comportamento contínuo do sistema. Dentro deste loop, a cada 2 segundos, o estado do pino de saída é alternado chamando a função mudar_estado_saida(). Em seguida, o estado do pino de entrada é alterado chamando a função mudar_estado_entrada(). Após cada alteração, o estado atual do pino de entrada é impresso na tela.

### Gestão de Interrupção de Teclado
Uma exceção KeyboardInterrupt é utilizada para interromper o teste quando o usuário pressiona Ctrl+C. Quando isso ocorre, uma mensagem é exibida indicando que o teste foi interrompido pelo usuário.
## Documentação📚

[Documentação](https://github.com/JoaoPedrowilliam/Teste-pratico)


## Stack utilizada💻

**Python:**  Biblioteca time

**tinkercad:** Card Arduino

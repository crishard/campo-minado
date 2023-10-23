# Este repositório tem como finalidade o desenvolvimento de um campo minado, o qual sera utilizado para as avaliações da disciplina de Tópicos Especiais II, a qual estamos abordando o tema de testes de software

## Requisitos

1. O software deve exibir um menu com todas as opções do jogo ao jogador e deve permitir que o jogador inicie um novo jogo escolhendo o nível de dificuldade.
    + Testar se o botão de nível fácil está sendo criado. ✔️
    + Testar se o botão de nível intermediário está sendo criado. ✔️
    + Testar se o botão de nível difícil está sendo criado. ✔️

2. O jogo deve contar com mais opções em seu menu inicial
    + Testar se ele pode escolher visualizar o tutorial
    + Testar se ele pode escolher visualizar o histórico
    + Testar se ele pode escolher fechar o jogo a partir desse menu

3. Deve ser possível selecionar o nível fácil
4. Deve ser possível selecionar o nível intermediário
5. Deve ser possível selecionar o nível difícil

6. o tabuleiro deve iniciar coberto e sem bandeiras
    + Testar se o software está criando o tabuleiro coberto
    + Testar se o software cria tabuleiros com bandeiras
    + Testar se o software cria tabuleiros sem bandeiras

7. O jogo deve ter um tabuleiro de jogo com dimensões 8x8 para o nível fácil
    + Testar se o jogo em "Fácil" tem 8 linhas
    + Testar se o jogo em “Fácil” tem 8 colunas.
    + Testar se o tabuleiro está vazio no início.
    + Testar se é possível marcar no tabuleiro.
    + Testar se a posição de jogada está dentro do tabuleiro.
    + Testar se o jogo inicia exibindo o time da partida
    + Testar se o jogo deixa visível o botão de pausa da partida
    + Testar se o jogo deixa visível o botão de abandonar a partida
    + Testar se o jogo deixa visível o botão de reiniciar a partida

8. O jogo deve ter um tabuleiro de jogo com dimensões 10x16 para intermediário
    + Testar se o jogo em “Intermediário” tem 10 linhas.
    + Testar se o jogo em “Intermediário” tem 16 colunas.
    + Testar se o tabuleiro está vazio no início ✔️
    + Testar se é possível marcar no tabuleiro ✔️
    + Testar se a posição de jogada está dentro do tabuleiro ✔️
    + Testar se o jogo inicia exibindo o time da partida
    + testar se o jogo deixa visível o botão de pausa da partida
    + Testar se o jogo deixa visível o botão de abandonar a partida
    + Testar se o jogo deixa visível o botão de reiniciar a partida

9. O jogo deve ter um tabuleiro de jogo com dimensões 24x24 para difícil.
    + Testar se o jogo em “Difícil” tem 24 linhas ✔️
    + Testar se o jogo em “Difícil” tem 24 colunas ✔️
    + Testar se o tabuleiro está vazio no início ✔️
    + Testar se é possível marcar no tabuleiro ✔️
    + Testar se a posição de jogada está dentro do tabuleiro ✔️
    + Testar se o jogo inicia exibindo o time da partida
    + testar se o jogo deixa visível o botão de pausa da partida
    + Testar se o jogo deixa visível o botão de abandonar a partida
    + Testar se o jogo deixa visível o botão de reiniciar a partida

10. O número de bombas no tabuleiro deve ser fixo 10 bombas para fácil.
    + Testar se o número de bombas do tabuleiro é maior que 10 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 10 ✔️
    + Testar se o número de bombas é igual a 10
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar, então são 3 casos de teste, um para string, outro para boolean e outro para inválido) ✔️
    + Testar se existem espaços suficientes para as bombas ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

11. O número de bombas no tabuleiro deve ser fixo 30 bombas para intermediário.
    + Testar se o número de bombas do tabuleiro é maior que 30 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 30 ✔️
    + Testar se o número de bombas é igual a 30
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar, então são 3 casos de teste, um para string, outro para boolean e outro para inválido) ✔️
    + Testar se existem espaços suficientes para as bombas ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

12. O número de bombas no tabuleiro deve ser fixo 100 bombas para difícil.
    + Testar se o número de bombas do tabuleiro é maior que 100 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 100 ✔️
    + Testar se o número de bombas é igual a 100
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar, então são 3 casos de teste, um para string, outro para boolean e outro para inválido) ✔️
    + Testar se existem espaços suficientes para as bombas ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

13. As bombas devem ser organizadas de forma aleatória dentro do tabuleiro
    + Testar se todas as bombas estão dentro do tabuleiro
    + Testar se alguma bomba está sendo colocada fora do tabuleiro
    + Testar se as bombas estão sendo organizadas de forma aleatória

14. O jogador deve ser informado sobre o número de bombas no tabuleiro antes de iniciar o jogo.
    + Testar se o tabuleiro é gerado  ✔️
    + Testar se as bombas são distribuídas de forma aleatória  ✔️
    + Testar se o número de bombas está sendo exibido em tempo real

15. Todas as zonas do tabuleiro devem começar cobertas e sem bandeira.
    + Verificar se as zonas estão todas cobertas ✔️
    + Verificar se nenhuma zona tem bandeira ✔️
    + Testar se as zonas estão descobertas

16. O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
    + Testar se é possível adicionar uma bandeira ✔️
    + Testar se a zona está coberta ✔️
    + Testar se a zona está descoberta ✔️
    + Testar se a posição clicada está dentro do tabuleiro ✔️
    + Testar se a bandeira foi adicionada corretamente
    + Testar se o número de bandeiras disponíveis foi atualizado

17. O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona.
    + verificar se a zona que ele clicou é uma zona com bandeira ✔️
    + verificar se a zona que ele clicou é uma zona descoberta ✔️
    + verificar se a zona que ele clicou é uma zona coberta ✔️
    + Testar se a bandeira foi removida após o click ✔️

18. O jogador deve ser capaz de descobrir uma zona que não tenha uma bandeira.
    + verificar se a zona que ele clicou tem bandeira ✔️
    + verificar se a zona que ele clicou já está descoberta ✔️
    + verificar se a zona que ele clicou está coberta. ✔️
    + verificar se a zona que ele clicou contém bomba ✔️
    + Testar se a zona foi descoberta após o click ✔️

19. O jogador não deve ser capaz de descobrir uma zona que contenha uma bandeira
    + verificar se a zona que ele clicou tem bandeira ✔️
    + verificar se a zona que ele clicou já está descoberta ✔️
    + verificar se a zona que ele clicou está coberta. ✔️
    + verificar se a zona que ele clicou contém bomba ✔️
    + Testar se a zona foi descoberta após o click ✔️
    + Tetar se o estado da zona ficou inalterado após o click

20. O usuário deve conseguir acessar um tutorial do jogo
    + Testar se o botão de tutorial está visível para o jogador
    + Testar se o tutorial está sendo exibido corretamente  ✔️
    + Testar se o botão de voltar para o menu funciona corretamente ✔️

21. O jogo deve revelar o número de bombas adjacentes a uma zona quando ela for descoberta.
    + Testar se a zona clicada possuí bandeira
    + verificar se a zona clicada contém bomba. ✔️
    + Testar se existe uma bomba adjacente a a zona clicada ✔️
    + Testar se não existe bomba adjacente a zona clicada ✔️

22. O software deve mostrar o tempo decorrido durante a partida.
    + Testar se o time do jogo esta sendo exibido corretamente
    + Testar se o time do jogo está sendo atualizado corretamente
    + Testar se o time consegue exibir o tempo após um longo período de partida

23. Deve haver um botão de pausa visível durante o jogo.
    + Testar se o botão de pausa está sendo criado corretamente ✔️
    + Testar se o botão começa como a label pause ✔️
    + Testar se o botão de retomar a partida está sendo criado corretamente ✔️
    + Testa se após o termino da partida o botão de pausa é desabilitado ✔️
    + Testa se a mensagem de jogo terminado aparece corretamente ✔️
    + Testar se o jogo inicia sem o botão de pausa ✔️
    + Testar se é possível pausar a partida ✔️
    + Testar se é possível retomar a partida ✔️
    + Testar se é possível descobrir uma zona com a partida pausada ✔️
    + Testar se a pausa e retomar nao alteram o tempo antes do inicio da partida ✔️
    + Testar se o pausa e retomar nao afeta o tempo depois que o jogo terminou ✔️
    + Testar se o pause/retomar afeta o tempo se ele foi começado manualmente ✔️
    + Testar se é possível adicionar uma bandeira com a partida pausada ✔️
    + Testar se é possível remover uma bandeira com a partida pausada ✔️
    + Testar se o usuário está sendo informado que a partida está pausada ✔️
    + Testar a performance do botão de pausa durante o jogo
        + Testar se o botão de pausa funciona corretamente após diversos clicks em pausa e retomar
        + testar se o botão de pausa funciona corretamente após o jogo permanecer em andamento durante um longo período de tempo
        + Testar se o botão de retomar funciona corretamente após o jogo permanecer pausado após um longo período de tempo
    + Testar se a label do botão de pausa e retomar é atualizado corretamente após divisas ações de pausar e retomar
    + Testar se a informação de partida pausada é informada ao usuário quando a partida está pausada
    + Testar se a informação de partida pausa é removida corretamente quando o jogador retoma a partida
    + Testar se o time da partida é pausado corretamente quando o botão de pausa é clicado
    + Testar se o time da partida volta a atualizar corretamente com a partida em andamento
    + Testes de performance do time com o botão pause:
        + Testar se o time volta a atualizar corretamente após a partida ficar pausada um longo período de tempo
        + Testar se time pausa corretamente após a partida ficar em andamento durante um longo período de tempo

24. Com a partida pausada, deve haver um botão de retomar visível durante o jogo

25. O jogador não deve conseguir realizar nenhuma ação no jogo com a partida pausada

26. Deve ser exibida uma mensagem para o jogador quando a partida estiver pausada

27. O  time do jogo deve permanecer inalterado enquanto a partida estiver pausada

28. O time do jogo deve continuar assim que a partida for retomada

29. Após a partida ser dada como encerrada, o botão de pausa deve permanecer desabilitado

30. Assim que a partida for finalizada, o time deve ser parado

31. Em caso de vitória, deve ser exibida uma mensagem de vitória com o tempo de partida do jogador

32. Em caso de derrota, o time da partida não deve ser salvo

33. Deve haver uma opção de tutorial para ensinar as regras básicas do jogo aos novos jogadores.
    + Testar se o botão de tutorial está sendo criado corretamente ✔️
    + Testar se a janela de tutorial está sendo criada corretamente ✔️
    + Testar se é possível voltar ao menu após abrir a janela de tutorial ✔️

34. Deve haver uma opção de retornar ao menu de escolha de nível a partir do tutorial

35. O software deve exibir o número de bandeiras disponíveis para uso.
    + Verificar se o software informa o número de bandeiras disponíveis antes de iniciar a partida ✔️
    + Testar se o software atualiza o número de bandeiras disponíveis quando uma bandeira é adicionada
    + Testar se o software atualiza o número de bandeiras disponíveis quando uma bandeira é removida
    + Verificar se o software informa em tempo real o número de bandeiras disponíveis

36. O número de bandeiras deve ser igual ao número de bombas

37. Após adicionar uma bandeira no tabuleiro, o número de bandeiras deve ser atualizado

38. Após remover uma bandeira no tabuleiro, o número de bandeiras deve ser atualizado

39. O jogador deve ser notificado imediatamente se descobrir uma zona que contenha uma bomba, indicando que a bomba explodiu, e que ele perdeu a partida.
    + Testar se o jogador descobriu uma zona com bomba ✔️
    + Testar se o popup de derrota está sendo criado corretamente ✔️
    + Testar se a partida está encerrada após descobrir uma zona com bomba  ✔️
    + Testar se é possível voltar ao menu a partir do popup de derrota ✔️
    + Testar se é possível jogar novamente após uma derrota

40. O software deve fornecer uma mensagem de vitória quando todas as áreas sem bombas forem descobertas corretamente.
    + verificar se existe alguma bomba descoberta  ✔️
    + verificar se existe alguma zona sem bomba coberta  ✔️
    + verificar se a mensagem de vitória está sendo exibida corretamente  ✔️
    + verificar se o usuário retorna ao menu inicial após a mensagem de vitória  ✔️
    + Testar se é possível jogar novamente após essa vitória  ✔️
    + Testar se a partida foi salva no histórico após a partida ✔️

41. O software deve fornecer a opção de voltar para o menu a partir da mensagem de vitória
42. O software deve fornecer a opção de jogar novamente a partir da mensagem de vitória

43. O software deve fornecer uma mensagem de derrota quando uma zona com bomba for descoberta.
44. O software deve fornecer a opção de voltar para o menu a partir da mensagem de derrota
45. O software deve fornecer a opção de jogar novamente a partir da mensagem de derrota

46. O software deve verificar se o jogador venceu a partida após cada ação.
    + Verifica se o jogo é encerrado quando uma bomba é clicada ✔️
    + Verifica se o jogo continua quando um local seguro é clicado ✔️
    + Verifica se o jogo não é afetado quando um local marcado com bandeira é clicado ✔️
    + Verificar se o jogo continua quando uma célula descoberta é clicada ✔️
    + Verificar se a zona clicada é a última que falta para ser descoberta ✔️
    + verificar se todas as zonas que não contém bomba estão descobertas ✔️
    + Verificar se o jogador vence ao revelar todas as zonas ✔️

47. O software deve fornecer um time com o tempo de jogo
    + Verifique se o tempo é atualizado corretamente quando o jogo está em andamento ✔️
    + Verifique se o tempo não é atualizado quando o jogo está pausado ✔️
    + Verifique se o tempo não é atualizado quando o jogo está encerrado ✔️
    + Verifique se o tempo é atualizado corretamente quando o jogador vence ✔️
    + Verifique se o botão de pausa alterna corretamente o time para pausado ✔️
    + Verifique se o botão de pausa funciona após o início do jogo ✔️
    + Verifique se o time é marcado como encerrado e as bombas são reveladas corretamente ✔️
    + Testar se a partida e inciada se o time for iniciado manualmente ✔️

48. Deve ser possível abandonar a partida a qualquer momento
    + Testar se o botão de abandonar a partida está sendo criado corretamente ✔️
    + Testar se é possível abandonar a partida ✔️
    + Testar se é possível abandonar a partida antes de iniciá-la ✔️
    + Testar se é possível abandonar a partida pausada ✔️
    + Testar se é possível abandonar a partida depois de um longo tempo de jogo ✔️
49. Deve ser possível visualizar o menu inicial após abandonar a partida

50. Deve ser possível revelar células adjacentes a uma célula que nao é adjacente a nenhum bomba.
    + Testar quando o valor da célula é igual a 0 ✔️
    + Testar quando a célula é uma bomba ✔️
    + Testar quando a célula contém bombas adjacentes ✔️
    + Testar quando todas as células adjacentes são bombas ✔️

51. Deve ser exibido um popup de em caso de vitória do usuário.
    + Testar se o popup está sendo criado corretamente
    + Testar se o popup exibe o tempo de vitória da partida
    + Testar se o popup cria o botão retornar ao menu corretamente
    + Testar o comportamento do botão de retornar ao menu
    + Testar se o popup cria o botão de jogar novamente corretamente
    + Testar o comportamento do botão de jogar novamente
    + Testar se o popup cria o botão de sair do jogo
    + Testar o comportamento do botão de sair do jogo

52. Deve ser exibido um popup de em caso de derrota do usuário.
    + Testar se o popup está sendo criado corretamente
    + Testar se o popup exibe o tempo de derrota da partida
    + Testar se o popup cria o botão retornar ao menu corretamente
    + Testar o comportamento do botão de retornar ao menu
    + Testar se o popup cria o botão de jogar novamente corretamente
    + Testar o comportamento do botão de jogar novamente
    + Testar se o popup cria o botão de sair do jogo
    + Testar o comportamento do botão de sair do jogo

53. O software deve contar com um ranking onde a pontuação é o tempo de jogo
    + Testar a contagem de tempo, verificar se o cronômetro inicia corretamente
    + Verificar se a opção de Ranking está visível no início da partida
    + Testar se é possível visualizar o Ranking
    + Testar se após uma vitória, o resultado é guardado no Ranking
    + Testar se o ranking está sendo exibido de forma correta

54. Cada zona pode ter de zero (0) a oito (8)zonas que contém bomba adjacentes a ela nível fácil
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testes para o calculo de adjacência do tabuleiro completo
        + Testar para um tabuleiro sem bombas
        + Testar para um tabuleiro que só contenha bombas
        + Testar para um tabuleiro com o número correto de bombas do nível
        + Testar para um tabuleiro com mais bombas que o esperado
        + Testar para um tabuleiro com bombas somente nas bordas
        + Testar para um tabuleiro com bombas somente no centro do tabuleiro

55. Cada zona pode ter de zero (0) a oito (8)zonas que contém bomba adjacentes a ela nível intermediário
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testes para o calculo de adjacência do tabuleiro completo
        + Testar para um tabuleiro sem bombas
        + Testar para um tabuleiro que só contenha bombas
        + Testar para um tabuleiro com o número correto de bombas do nível
        + Testar para um tabuleiro com mais bombas que o esperado
        + Testar para um tabuleiro com bombas somente nas bordas
        + Testar para um tabuleiro com bombas somente no centro do tabuleiro

56. Cada zona pode ter de zero (0) a oito (8)zonas que contém bomba adjacentes a ela nível difícil
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testes para o calculo de adjacência do tabuleiro completo
        + Testar para um tabuleiro sem bombas
        + Testar para um tabuleiro que só contenha bombas
        + Testar para um tabuleiro com o número correto de bombas do nível
        + Testar para um tabuleiro com mais bombas que o esperado
        + Testar para um tabuleiro com bombas somente nas bordas
        + Testar para um tabuleiro com bombas somente no centro do tabuleiro

57. Após uma derrota todas as bombas do tabuleiro devem ser exibidas - nível fácil
58. Após uma derrota todas as bombas do tabuleiro devem ser exibidas - nível intermediário
59. Após uma derrota todas as bombas do tabuleiro devem ser exibidas - nível difícil

60. Ao clicar em uma célula cujo valor é zero, devem ser reveladas todas as células adjacentes a ela até que seja encontrado um valor diferente de 0 - para o nível fácil
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testar em tabuleiros criados aleatoriamente para o nível fácil, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível intermediário, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível difícil, se o resultado é o esperado

61. Ao clicar em uma célula cujo valor é zero, devem ser reveladas todas as células adjacentes a ela até que seja encontrado um valor diferente de 0 - nível intermediário
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testar em tabuleiros criados aleatoriamente para o nível fácil, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível intermediário, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível difícil, se o resultado é o esperado

62. Ao clicar em uma célula cujo valor é zero, devem ser reveladas todas as células adjacentes a ela até que seja 
encontrado um valor diferente de 0 - nível difícil
    + Testar uma zona sem bombas adjacentes
    + Testar uma zona com uma bomba adjacente
    + Testar uma sona com duas bombas adjacentes
    + Testar uma sona com três bombas adjacentes
    + Testar uma sona com quatro bombas adjacentes
    + Testar uma sona com cinco bombas adjacentes
    + Testar uma sona com seis bombas adjacentes
    + Testar uma sona com sete bombas adjacentes
    + Testar uma sona com oito bombas adjacentes
    + Testar em tabuleiros criados aleatoriamente para o nível fácil, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível intermediário, se o resultado é o esperado
    + Testar em tabuleiros criados aleatoriamente para o nível difícil, se o resultado é o esperado

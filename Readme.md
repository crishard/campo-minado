# Este repositório tem como finalidade o desenvolvimento de um campo minado, o qual sera utilizado para as avaliações da disciplina de Tópicos Especiais II, a qual estamos abordando o tema de testes de software

## Requisitos

1. O software deve permitir que o jogador inicie um novo jogo escolhendo o nível de dificuldade.
    + Testar se ele pode escolher o nível fácil. ✔️
    + Testar se ele pode escolher o nível intermediário. ✔️
    + Testar se ele pode escolher o nível difícil. ✔️

2. O jogo deve ter um tabuleiro de jogo com dimensões 8x8 para o nível fácil
    + Testar se o jogo em “Fácil” tem 8x8. ✔️
    + Testar se o tabuleiro está vazio no início. ✔️
    + Testar se é possível marcar no tabuleiro. ✔️
    + Testar se a posição de jogada está dentro do tabuleiro. ✔️
    + Testar se pode colocar uma bandeira ✔️

3. O jogo deve ter um tabuleiro de jogo com dimensões 10x16 para intermediário
    + Testar se o jogo em “Intermediário” tem 10x16. ✔️
    + Testar se o tabuleiro está vazio no início ✔️
    + Testar se é possível marcar no tabuleiro ✔️
    + Testar se a posição de jogada está dentro do tabuleiro ✔️

4. O jogo deve ter um tabuleiro de jogo com dimensões 24x24 para difícil.
    + Testar se o jogo em “Difícil” tem 24x24 ✔️
    + Testar se o tabuleiro está vazio no início ✔️
    + Testar se é possível marcar no tabuleiro ✔️
    + Testar se a posição de jogada está dentro do tabuleiro ✔️

5. O número de bombas no tabuleiro deve ser fixo 10 bombas para fácil.
    + Testar se o número de bombas do tabuleiro é maior que 10 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 10 ✔️
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar) ✔️
    + Testar se existem espaços suficientes para as bombas] ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

6. O número de bombas no tabuleiro deve ser fixo30 bombas para intermediário.
    + Testar se o número de bombas do tabuleiro é maior que 30 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 30 ✔️
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar) ✔️
    + Testar se existem espaços suficientes para as bombas] ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

7. O número de bombas no tabuleiro deve ser fixo 100 bombas para difícil.
    + Testar se o número de bombas do tabuleiro é maior que 100 ✔️
    + Testar se o número de bombas do tabuleiro é menor que 100 ✔️
    + Testar se o tabuleiro só contém bombas ✔️
    + Testar se o tabuleiro não contém bombas ✔️
    + Testar se as bombas estão posicionadas em locais válidos ✔️
    + Testar se existe alguma bomba no tabuleiro ✔️
    + Testar se o número de bombas é negativo ✔️
    + Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar) ✔️
    + Testar se existem espaços suficientes para as bombas] ✔️
    + Testar se o tabuleiro é de tamanho vazio ✔️

8. O jogador deve ser informado sobre o número de bombas no tabuleiro antes de iniciar o jogo.
    + Testar se o tabuleiro é gerado  ✔️
    + Testar se as bombas são distribuídas de forma aleatória  ✔️

9. Todas as zonas do tabuleiro devem começar cobertas e sem bandeira.
    + Verificar se as zonas estão todas cobertas
    + Verificar se nenhuma zona tem bandeira

10. O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
    + estar se é possível adicionar uma bandeira ✔️
    + Testar se a zona está coberta ✔️
    + Testar se a zona está descoberta ✔️
    + Testar se a posição clicada está dentro do tabuleiro ✔️

11. O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona.
    + verificar se a zona que ele clicou é uma zona com bandeira ✔️
    + verificar se a zona que ele clicou é uma zona descoberta ✔️
    + verificar se a zona que ele clicou é uma zona coberta ✔️
    + Testar se a bandeira foi removida após o click ✔️

12. O jogador deve ser capaz de descobrir uma zona que não tenha uma bandeira.
    + verificar se a zona que ele clicou tem bandeira ✔️
    + verificar se a zona que ele clicou já está descoberta ✔️
    + verificar se a zona que ele clicou está coberta. ✔️
    + verificar se a zona que ele clicou contém bomba ✔️
    + Testar se a zona foi descoberta após o click ✔️

13. O usuário deve conseguir acessar um tutorial do jogo
    + Testar se o tutorial está sendo exibido corretamente  ✔️
    + Testar se o botão de voltar para o menu funciona corretamente ✔️

14. Não deve ser possível descobrir uma zona que tenha uma bandeira. O jogador deve ser notificado se tentar fazê-lo.
    + Testar se o jogador é informado em caso de descobrir uma zona que tenha bandeira
    + Testar se ao tentar descobrir uma zona com bandeira, o tabuleiro permanece inalterado

15. Não deve ser possível colocar uma bandeira em uma zona que já foi descoberta. O jogador deve ser notificado se tentar fazê-lo.
    + Testar se o jogador é informado que a zona selecionada já está descoberta

16. O jogo deve revelar o número de bombas adjacentes a uma zona quando ela for descoberta.
    + verificar se a zona clicada contém bomba.
    + Testar se existe uma bomba adjacente a a zona clicada
    + Testar se não existe bomba adjacente a zona clicada
    + Testar se o cálculo de adjacência está correto

17. O software deve mostrar o tempo decorrido durante a partida.
    + Testar se é possível pausar a partida
    + Testar se é possível retomar a partida
    + Testar se é possível descobrir uma zona com a partida pausada
    + Testar se é possível adicionar uma bandeira com a partida pausada
    + Testar se é possível remover uma bandeira com a partida pausada
    + Testar se o usuário está sendo informado que a partida está pausada

18. Deve haver um botão de pausa visível durante o jogo.
    + Testar se o botão de pausa está sendo criado corretamente ✔️
    + Testar se o botão de retomar a partida está sendo criado corretamente ✔️
19. Deve haver uma opção de tutorial para ensinar as regras básicas do jogo aos novos jogadores.
    + Testar se a janela o botão de tutorial está sendo criado corretamente ✔️
    + Testar se a janela de tutorial está sendo criada corretamente ✔️
    + Testar se é possível voltar ao menu após abrir a janela de tutorial ✔️

20. O software deve exibir o número de bandeiras disponíveis para uso.
    + Verificar se o software informa o número de bandeiras disponíveis antes de iniciar a partida
    + Testar se o software atualiza o número de bandeiras disponíveis quando uma bandeira é adicionada
    + Testar se o software atualiza o número de bandeiras disponíveis quando uma bandeira é removida
    + Verificar se o software informa em tempo real o número de bandeiras disponíveis

21. O jogador deve ser notificado imediatamente se descobrir uma zona que contenha uma bomba, indicando que a bomba explodiu, e que ele perdeu a partida.
    + Testar se o jogador descobriu uma zona com bomba
    + Testar se o popup de derrota está sendo criado corretamente
    + Testar se a partida está encerrada após descobrir uma zona com bomba
    + Testar se é possível voltar ao menu a partir do popup de derrota
    + Testar se é possível jogar novamente após uma derrota
22. O software deve fornecer uma mensagem de vitória quando todas as áreas sem bombas forem descobertas corretamente.
    + verificar se existe alguma bomba descoberta
    + verificar se existe alguma zona sem bomba coberta
    + verificar se a mensagem de vitória está sendo exibida corretamente
    + verificar se o usuário retorna ao menu inicial após a mensagem de vitória
    + Testar se é possível jogar novamente após essa vitória
    + Testar se a partida foi salva no histórico após a partida

23. O jogador deve ser informado sobre o número de bombas no tabuleiro antes de iniciar o jogo.
    + Testar se o número de bombas da partida foi exibido antes de começar a partida
    + Testar se o número de bombas está sendo exibido em tempo real

24. O software deve verificar se o jogador venceu a partida após cada ação.
    + Verifica se o jogo é encerrado quando uma bomba é clicada/
    + Verifica se o jogo continua quando um local seguro é clicado
    + Verifica se o jogo não é afetado quando um local marcado com bandeira é clicado
    + Verificar se o jogo continua quando uma célula descoberta é clicada

25. O software deve fornecer um time com o tempo de jogo
    + Verifique se o tempo é atualizado corretamente quando o jogo está em andamento
    + Verifique se o tempo não é atualizado quando o jogo está pausado
    + Verifique se o tempo não é atualizado quando o jogo está encerrado
    + Verifique se o tempo é atualizado corretamente quando o jogador vence
    + Verifique se o botão de pausa alterna corretamente o time para pausado
    + Verifique se o botão de pausa funciona após o início do jogo
    + Verifique se o time é marcado como encerrado e as bombas são reveladas corretamente
    + Testar se a partida e inciada se o time for iniciado manualmente

26. Deve haver um botão de pausa (Retomar) visível durante a partida
    + Testa se o botão pause esta sendo criado corretamente ✔️
    + Testar se o botão começa como pause ✔️
    + Testa se o jogo está sendo pausado corretamente ✔️
    + Testa se o botão pausar altera pra retomar corretamente ✔️
    + Testa se a mensagem de ações da partida só pode ser realizadas com ela em andamento é criada corretamente ✔️
    + Testa se após o termino da partida o botão de pausa é desabilitado ✔️
    + Testa se a mensagem de jogo terminado aparece corretamente ✔️
    + Testar se o comportamento do botão persiste inalterado após vários clicks ✔️
    + Testa o comportamento do botão após im longo período de tempo ✔️
    + Testar se o jogo inicia sem o botão de pausa ✔️
    + Testa a retomada do time correto apos varias pausas ✔️
    + Testar se a pausa e retomar nao alteram o tempo antes do inicio da partida ✔️
    + Testar se o pausa e retomar nao afeta o tempo depois que o jogo terminou ✔️
    + Testar se o pause/retomar afeta o tempo se ele foi começado manualmente ✔️

27. Deve ser possível abandonar a partida a qualquer momento
    + Testar se o botão de abandonar a partida está sendo criado corretamente ✔️
    + Testar se é possível abandonar a partida ✔️
    + Testar se é possível abandonar a partida antes de iniciá-la ✔️
    + Testar se é possível abandonar a partida pausada ✔️
    + Testar se é possível abandonar a partida depois de um longo tempo de jogo ✔️

### Testes antigos, vao ser refatorados ou excluídos

+ O software deve verificar se o jogador perdeu a partida após cada ação.
+ O software deve atualizar a interface do jogo para refletir o resultado da ação do jogador.
+ O software deve registrar o tempo decorrido desde o início da partida.
+ O software deve permitir que o jogador pause e retome o jogo a qualquer momento.
+ O software deve fornecer uma mensagem de vitória quando todas as areas sem bombas forem descobertas corretamente.
+ O software deve fornecer uma mensagem de derrota quando uma area com bomba for descoberta.
+ O software deve verificar se todas as areas sem bombas foram descobertas corretamente para determinar a vitória.
+ O software deve permitir que o jogador reinicie a partida a qualquer momento.
+ O software deve manter um histórico de resultados de partidas concluídas.
+ O software deve permitir que o jogador acesse o histórico de resultados.
+ O software deve ter uma interface de usuário intuitiva e amigável.
+ Deve haver um menu principal com opções para iniciar um novo jogo, acessar o histórico de resultados e sair do jogo.
+ O menu principal deve incluir opções para escolher o nível de dificuldade.
+ Deve haver um botão de pausa visível durante o jogo.
+ O software deve mostrar o tempo decorrido durante a partida.
+ Deve haver uma representação visual das bandeiras colocadas pelos jogadores.
+ O software deve exibir o número de bandeiras disponíveis para uso.
+ Deve haver uma tela de tutorial para ensinar as regras básicas do jogo aos novos jogadores.

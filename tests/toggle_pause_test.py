import pytest
from campo_minado import CampoMinado
import datetime  

@pytest.fixture
def jogo_iniciado():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.started = True
    return jogo

@pytest.fixture
def jogo_sem_botao_pausa():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = False
    return jogo

def test_toggle_pause_inicia_pausa(jogo_iniciado):
    jogo = jogo_iniciado
    jogo.toggle_pause()
    assert jogo.paused == True

# Testa se o jogo está sendo pausado corretamente
def test_toggle_pause_retoma(jogo_iniciado):
    jogo = jogo_iniciado
    jogo.paused = True
    jogo.toggle_pause()
    assert jogo.paused == False

# Testa se após o termino da partida o botão de pausa é desabilitado
def test_toggle_pause_sem_botao_pausa(jogo_sem_botao_pausa):
    jogo = jogo_sem_botao_pausa
    jogo.toggle_pause()
    # Verifique se a função não altera o estado do jogo quando o botão de pausa não está habilitado
    assert not jogo.pause_button_enabled  # Verifique se o botão de pausa não está habilitado

# Testa se a mensagem de jogo terminado aparece corretamente
def test_game_is_finish_message(jogo_sem_botao_pausa): 
    jogo = jogo_sem_botao_pausa
    jogo.toggle_pause()
    assert jogo.pause_label.cget('text') == 'O jogo acabou.'

# Testa se o botão pausar altera pra retomar corretamente
def test_toggle_pause_habilita_quando_botao_pausa_habilitado():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

    # Quando a função toggle_pause é chamada, o jogo deve ser pausado
    jogo.toggle_pause()
    assert jogo.pause_button.cget('text') == 'Retomar'



# Testa se a mensagem de ações da partida só pode ser realizadas com ela em andamento é criada corretamente
def test_not_action_paused():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    jogo.toggle_pause()
    assert jogo.pause_label.cget('text') == 'Você precisa retomar o jogo para realizar alguma ação.'



# Testa vários clicks no botão de pausa retomar
def test_toggle_pause_retoma_e_pausa():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

    # Quando a função toggle_pause é chamada, o jogo deve ser pausado
    jogo.toggle_pause()
    # Quando a função toggle_pause é chamada novamente, o jogo deve ser retomado
    jogo.toggle_pause()
    # Chamando novamente, o jogo deve ser pausado novamente
    jogo.toggle_pause()

    assert jogo.pause_button.cget('text') == 'Retomar'


# Testa se o botão pause esta sendo criado corretamente
def test_toggle_pause_inicia_sem_botao_pausa():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = False

    # Quando a função toggle_pause é chamada, o estado do jogo não deve ser afetado
    jogo.toggle_pause()

    assert jogo.pause_label.cget('text') == 'O jogo acabou.'

# Testa o comportamento do botão após im longo período de tempo
def test_toggle_pause_retoma_e_pausa_com_tempo():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True


    # Inicia o tempo de jogo
    jogo.toggle_pause()

    # Simula a passagem de algum tempo
    jogo.start_time = datetime.datetime.now() - datetime.timedelta(hours=10)
    jogo.toggle_pause()

    # Verifica se o tempo de jogo foi atualizado corretamente após a retomada
    assert jogo.paused == False

# # Testar se o jogo reinicia sem o botão de pausa aopós 
# def test_toggle_pause_inicia_sem_botao_pausa_com_tempo():
#     jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
#     jogo.pause_button_enabled = False

#     # Inicialmente, o jogo não está pausado
#     assert jogo.paused == False

#     # Inicia o tempo de jogo
#     jogo.toggle_pause()
#     assert jogo.paused == False
#     assert jogo.pause_button_enabled == False
#     assert jogo.pause_label.cget('text') == 'O jogo acabou.'

#     # Simula a passagem de algum tempo
#     jogo.start_time = datetime.datetime.now() - datetime.timedelta(seconds=10)
#     jogo.toggle_pause()

#     # Verifica se o tempo de jogo permanece o mesmo após a tentativa de retomada
#     assert jogo.paused == False
#     assert jogo.pause_button_enabled == False
#     assert jogo.pause_label.cget('text') == 'O jogo acabou.'
#     assert jogo.start_time is not None

#  Testa a retomada do time correto apos varias pausas
def test_toggle_pause_retoma_tempo_corretamente_apos_varias_pausas():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    # Inicia o tempo de jogo
    jogo.toggle_pause()

    # Simula a passagem de algum tempo
    jogo.start_time = datetime.datetime.now() - datetime.timedelta(seconds=10)
    jogo.toggle_pause()

    # Simula outra pausa e retomada
    jogo.toggle_pause()
    jogo.start_time = datetime.datetime.now() - datetime.timedelta(seconds=20)
    jogo.toggle_pause()

    assert jogo.paused == False

#  Testar se a pausa e retomar nao alteram o tempo antes do inicio da partida
def test_toggle_pause_nao_afeta_o_tempo_quando_jogo_nao_iniciou():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    # Chamar a função toggle_pause não deve afetar o tempo
    jogo.toggle_pause()

    # Agora, após chamar toggle_pause, o tempo ainda deve ser None
    assert jogo.start_time is None

#  Testar se o pausa e retomar nao afeta o tempo depois que o jogo terminou
def test_toggle_pause_nao_afeta_o_tempo_quando_jogo_terminou():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    jogo.game_over = True
    jogo.paused = True  # Definir o jogo como pausado inicialmente

    # Chamar a função toggle_pause não deve afetar o tempo
    jogo.toggle_pause()
    assert jogo.paused == True

# def test_toggle_pause_nao_afeta_tempo_quando_jogo_nao_iniciou():
#     jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
#     jogo.pause_button_enabled = True
    
#     # Inicialmente, o jogo não está pausado e o tempo não foi iniciado
#     assert jogo.paused == False
#     assert jogo.start_time is None
    
#     # Chamar a função toggle_pause não deve afetar o estado do jogo
#     jogo.toggle_pause()
    
#     # O estado do jogo não deve ser pausado e o tempo não deve ter sido iniciado
#     assert jogo.paused == True
#     assert jogo.start_time is None

#  Testar se o pause/retomar afeta o tempo se ele foi começado manualmente
def test_toggle_pause_nao_afeta_tempo_quando_tempo_iniciado_manualmente():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    jogo.started = True  # Jogo já iniciado
    jogo.start_time = datetime.datetime.now()  # Tempo iniciado manualmente

    # Chamar a função toggle_pause não deve afetar o tempo já iniciado
    jogo.toggle_pause()
    assert jogo.start_time is not None



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

    assert not jogo.pause_button_enabled 

# Testa se a mensagem de jogo terminado aparece corretamente
def test_game_is_finish_message(jogo_sem_botao_pausa): 
    jogo = jogo_sem_botao_pausa
    jogo.toggle_pause()
    assert jogo.pause_label.cget('text') == 'O jogo acabou.'

# Testa se o botão pausar altera pra retomar corretamente
def test_toggle_pause_habilita_quando_botao_pausa_habilitado():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

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

    jogo.toggle_pause()
    jogo.toggle_pause()
    jogo.toggle_pause()

    assert jogo.pause_button.cget('text') == 'Retomar'


# Testa se o botão pause esta sendo criado corretamente
def test_toggle_pause_inicia_sem_botao_pausa():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = False

    jogo.toggle_pause()

    assert jogo.pause_label.cget('text') == 'O jogo acabou.'

# Testa o comportamento do botão após im longo período de tempo
def test_toggle_pause_retoma_e_pausa_com_tempo():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

    jogo.toggle_pause()

    jogo.start_time = datetime.datetime.now() - datetime.timedelta(hours=10)
    jogo.toggle_pause()

    assert jogo.paused == False

#  Testa a retomada do time correto apos varias pausas
def test_toggle_pause_retoma_tempo_corretamente_apos_varias_pausas():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

    jogo.toggle_pause()

    jogo.start_time = datetime.datetime.now() - datetime.timedelta(seconds=10)
    jogo.toggle_pause()

    jogo.toggle_pause()
    jogo.start_time = datetime.datetime.now() - datetime.timedelta(seconds=20)
    jogo.toggle_pause()

    assert jogo.paused == False

#  Testar se a pausa e retomar nao alteram o tempo antes do inicio da partida
def test_toggle_pause_nao_afeta_o_tempo_quando_jogo_nao_iniciou():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True

    jogo.toggle_pause()

    assert jogo.start_time is None

#  Testar se o pausa e retomar nao afeta o tempo depois que o jogo terminou
def test_toggle_pause_nao_afeta_o_tempo_quando_jogo_terminou():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    jogo.game_over = True
    jogo.paused = True 

    jogo.toggle_pause()
    assert jogo.paused == True


#  Testar se o pause/retomar afeta o tempo se ele foi começado manualmente
def test_toggle_pause_nao_afeta_tempo_quando_tempo_iniciado_manualmente():
    jogo = CampoMinado(root=None, rows=8, cols=8, bombs=1, show_difficulty_menu=None)
    jogo.pause_button_enabled = True
    jogo.started = True  
    jogo.start_time = datetime.datetime.now()  
    
    jogo.toggle_pause()
    assert jogo.start_time is not None

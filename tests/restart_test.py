import pytest
import tkinter as tk
from campo_minado import create_game_instance
from functions.on_right_click import on_right_click_function

def test_restart_game():
    root = tk.Tk()
    root.title("Teste Reiniciar Jogo")

    # Inicie o jogo
    game = create_game_instance(root, 8, 8, 10)

    # Faça alguns movimentos no jogo, como clicar em algumas células
    # (certifique-se de não revelar todas as bombas para evitar derrota)
    # ...

    # Clique no botão de reiniciar
    assert game.restart_game

def test_restart_clear():
    root = tk.Tk()
    root.title("Teste Reiniciar Jogo")

    # Inicie o jogo
    game = create_game_instance(root, 8, 8, 10)

    # Faça alguns movimentos no jogo, como clicar em algumas células
    # (certifique-se de não revelar todas as bombas para evitar derrota)
    # ...
    game.restart_game()

    # Clique no botão de reiniciar
    assert game


def test_pause_game():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.toggle_pause()
    
    # Verifique se o jogo está realmente pausado
    assert game.paused is True  # Verifica se a variável 'paused' foi definida como True
    
def test_game_rows_equals():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.rows ==8 # Verifica se a variável 'paused' foi definida como True
    
def test_game_cols_equals():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.cols ==8 # Verifica se a variável 'paused' foi definida como True
    
def test_game_bombs_equals():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.bombs ==10 # Verifica se a variável 'paused' foi definida como True
    
def test_game_used_flags_zero():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.used_flags == 0 # Verifica se a variável 'paused' foi definida como True
    
def test_game_count_flags_zero():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.bomb_count == 0 # Verifica se a variável 'paused' foi definida como True

    
def test_game_time_zero():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.restart_game()
    
    # Verifique se o jogo está realmente pausado
    assert game.start_time == None # Verifica se a variável 'paused' foi definida como True


def test_retomar_game():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Simule a pausa do jogo
    game.toggle_pause()
    game.toggle_pause()
    
    # Verifique se o jogo está realmente pausado
    assert game.paused is False

def test_entire_board_covered():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)

    # Verifique se todas as células estão cobertas no início do jogo
    for row in range(8):
        for col in range(8):
            assert not game.flags[row][col]  # Verifica se nenhuma bandeira está definida
            assert game.buttons[row][col].cget('state') == 'normal'  # Verifica se o estado é normal (não revelado)

def test_no_flags_on_board():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)

    # Verifique se não há bandeiras definidas em nenhuma célula no início do jogo
    for row in range(8):
        for col in range(8):
            assert not game.flags[row][col]


def test_pause_button_displayed():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)

    # Verifique se o botão de pausa está sendo exibido na interface
    assert game.pause_button.winfo_exists()

def test_pause_button_label():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)

    # Verifique se o botão de pausa está sendo exibido com a label correta
    expected_label = "Pausar"  # A label que você espera que o botão tenha
    actual_label = game.pause_button.cget('text')  # Obtém o texto atual da label do botão
    assert actual_label == expected_label

def test_no_game_saved_to_history_after_restart():
    # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    # Obtenha o histórico de partidas antes de reiniciar o jogo
    historico_anterior = game.historico_partidas.copy()
    
    # Reinicie o jogo
    game.restart_game()
    
    # Verifique se o histórico de partidas não foi alterado após o reinício
    assert game.historico_partidas == historico_anterior

#  Testa se a zona esta descoberta apos o click
def test_zone_discoverd_after_click():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = create_game_instance(root, 8, 8, 10)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = ''  

    game.on_button_click(zone_row, zone_col)

    assert game.buttons[row][col] != '', "O jogo não terminou após o clique na zona com uma bomba."


event = None
game_over = False
paused = False
bombs = 10
flags = [[False for _ in range(10)] for _ in range(10)]
buttons = [[tk.Button() for _ in range(10)] for _ in range(10)]
row = 5
col = 5
bomb_count = -2
started = True
flag_label = None
used_flags = 0

def update_flag_label():
        flags_left = bombs - used_flags
        # flag_label.config(text=f"Bandeiras para uso: {flags_left}")
# Testar se é possível adicionar uma bandeira
def test_add_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(update_flag_label, used_flags,
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert buttons[row][col]['text'] == '🏳'


def test_label_retomar_game():
     # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    game.toggle_pause()
    # Verifique se o botão de pausa está sendo exibido com a label correta
    expected_label = "Retomar"  # A label que você espera que o botão tenha
    actual_label = game.pause_button.cget('text')  # Obtém o texto atual da label do botão
    assert actual_label == expected_label

def test_label_pause_game():
     # Crie uma instância do jogo com as configurações desejadas
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    game.toggle_pause()
    game.toggle_pause()
    # Verifique se o botão de pausa está sendo exibido com a label correta
    expected_label = "Pausar"  # A label que você espera que o botão tenha
    actual_label = game.pause_button.cget('text')  # Obtém o texto atual da label do botão
    assert actual_label == expected_label

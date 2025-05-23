#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from noelcpm import CPMnoelcpm

__CHANNEL_USERNAME__ = "@Henriquefxp7"
__GROUP_USERNAME__   = "81973061449"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "ATENCAO PARA USAR A FERRAMENTA E NECESSARIO ADICIONAR CREDITOS COM O ADM Henriquefxp7."
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐅𝐀𝐂𝐀 𝐋𝐎𝐆𝐎𝐔𝐓 𝐃𝐎 𝐂𝐏𝐌 𝐀𝐍𝐓𝐄𝐒 𝐃𝐄 𝐔𝐒𝐀𝐑 𝐄𝐒𝐓𝐀 𝐅𝐄𝐑𝐑𝐀𝐌𝐄𝐍𝐓𝐀'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐂𝐎𝐌𝐏𝐀𝐑𝐓𝐈𝐋𝐇𝐀𝐑 𝐀 𝐂𝐇𝐀𝐕𝐄 𝐃𝐄 𝐀𝐂𝐄𝐒𝐒𝐎 𝐍𝐀𝐎 𝐄 𝐏𝐄𝐑𝐌𝐈𝐓𝐈𝐃𝐎 𝐒𝐄𝐑𝐀 𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐃𝐎'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           INSTAGRAM: @{__CHANNEL_USERNAME__} WHATSAPP @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ INFORMACOES DO JOGADOR]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'NOME   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'SEU ID NO JOGO: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'DINHEIRO  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'GOLDS : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ 𝐃𝐄𝐓𝐀𝐋𝐇𝐄𝐒 𝐃𝐀 𝐂𝐇𝐀𝐕𝐄 𝐃𝐄 𝐀𝐂𝐄𝐒𝐒𝐎]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'CHAVE DE ACESSO : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'ID DO TELEGRAM: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'SEU SALDO $  : {(data.get("coins") if not data.get("is_unlimited") else "ilimitado")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} cannot be empty or just spaces. Please try again.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝙇𝙤𝙘𝙖𝙡𝙞𝙯𝙖𝙘𝙖𝙤 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'ENDERECO IP : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'CIDADE  : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'PAIS  : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] INSIRA SEU EMAIL[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] INSIRA SUA SENHA[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] INSIRA SUA CHAVE DE ACESSO[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMnoelcpm(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ESSA CONTA NAO EXISTE.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'SENHA INVALIDA.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'CHAVE DE ACESSO INVALIDA.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                print(Colorate.Horizontal(Colors.rainbow, '! ATENCAO: BANCO DE DADOS LOTADO, FALE COM O SUPORTE  !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: ADICIONAR DINHEIRO           1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: ADICIONAR GOLDS              3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: INSERIR RANK KING            4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: MUDAR ID                     3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: MUDAR NOME                   100 '))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: MUDAR NOME ( RGB )           100'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: NUMEROS PLACAS               2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: DELETAR CONTA                GRATIS '))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: REGISTRAR CONTA              GRATIS'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: DELETAR AMIGOS               500'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: DESBLOQUEAR CARROS PAGOS     4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: DESBLOQUEAR TODOS CARROS     3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: SIRENE EM TODOS CARROS       2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: DESBLOQUEAR W16              3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: DESBLOQUEAR BUZINAS          3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: MOTOR NAO QUEBRA             2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: GASOLINA INFINITA            2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: DESBLOQUEAR CASA 3           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: DESBLOQUEAR FUMACA           2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: DESBLOQUEAR ANIMAÇÕES        2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: DESBLOQUEAR RODAS            4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: DESBLOQUEAR ROUPAS MASCULINAS 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: DESBLOQUEAR ROUPAS FEMININAS  3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: ALTERAR CORRIDAS GANHAS      1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: ALTERAR CORRIDAS PERDIDAS    1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: CLONAR CONTA                 5.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : SAIR'.format(opcao))
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            service = IntPrompt.ask(f"[bold][?] SELECIONE UM SERVICO [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'VOLTE SEMPRE....: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSIRA A QUANTIDADE DE DINHEIRO QUE DESEJA ADICIONAR .'))
                amount = IntPrompt.ask("[?] QUANTIDADE")
                console.print("[%] SALVANDO DADOS: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE  Y PARA SIM E N PARA NAO ", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f' VOLTE SEMPRE : @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA .'))
                    print(Colorate.Horizontal(Colors.rainbow, 'ULTILIZE VALORES VALIDOS.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSIRA A QUANTIDADE DE GOLDS QUE DESEJA ADICIONAR.'))
                amount = IntPrompt.ask("[?] QUANTIDADE")
                console.print("[%] SALVANDO DADOS: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE  Y PARA SIM E N PARA NAO ", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f' VOLTE SEMPRE : @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'USE VALORES VALIDOS.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] ATENCAO:[/bold red]: SE O KING NAO APARECER, SAIA E ABRA O JOGO ALGUMAS VEZES.", end=None)
                console.print("[bold red][!] ATENCAO:[/bold red]: POR FAVOR NAO DESBLOQUIE O KING NA MESMA CONTA DUAS VEZES.", end=None)
                sleep(2)
                console.print("[%] ADICIONANDO O KING NA SUA CONTA: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'VOLTE SEMPRE....: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSIRA SEU NOVO ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] SALVANDO DADOS: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE  Y PARA SIM E N PARA NAO ", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f' VOLTE SEMPRE : @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'ESSE ID JA ESTA EM USO TENTE OUTRO.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSIRA SEU NOVO NOME.'))
                new_name = Prompt.ask("[?] NOME")
                console.print("[%] SALVANDO DADOS: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE  Y PARA SIM E N PARA NAO ", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f' VOLTE SEMPRE : @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'USE VALORES VALIDOS.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSIRA SEU NOVO NOME ( RGB ).'))
                new_name = Prompt.ask("[?] NOME")
                console.print("[%] SALVANDO DADOS: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE  Y PARA SIM E N PARA NAO ", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f' VOLTE SEMPRE : @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'USE VALORES VALIDOS.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] ADICIONANDO NUMERO AS PLACAS: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCESSO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'VOLTR SEMPRE....: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                    sleep(2)
                    continue
            elif service == 8: #

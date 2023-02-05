import os
import requests, pystyle, json
from pystyle import Colors, Colorate 


def clear_screen():
    print('\033c')

def display_logo(input_text):
    logo = """
                                    
                                            ██     ██  ██████   ██████ ██   ██ 
                                            ██     ██ ██    ██ ██      ██  ██  
                                            ██  █  ██ ██    ██ ██      █████   
                                            ██ ███ ██ ██    ██ ██      ██  ██  
                                             ███ ███   ██████   ██████ ██   ██ 
                                                                            
                                   
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

"""
    print(Colorate.Horizontal(Colors.blue_to_purple, logo, 1))
   # print('\n' + ' ' * ((71 - len(input_text))//1) + input_text + '\n\n')
    print('\n\n' + input_text.center(121))

def get_webhook_url():
    clear_screen()
    display_logo('Enter the Webhook URL: ')
    return input("                                                           ")

def get_webhook_name():
    clear_screen()
    display_logo('Enter the Webhook Name: ')
    return input("                                                          ")

def get_thread_id():
    clear_screen()
    display_logo('Enter the Thread ID: ')
    return input("                                                     ")

def get_avatar_url():
    clear_screen()
    display_logo('Enter the Avatar URL: ')
    return input("                                                           ")

def get_json_file_path():
    clear_screen()
    display_logo("Enter the path to the JSON file: ")
    return input("                                                           ")

def post_thread_message(webhook_url, json_file_path, webhook_name=None, thread_id=None, avatar_url=None):
    with open(json_file_path) as f:
        payload = json.load(f)

    if webhook_name:
        payload['username'] = webhook_name
    if avatar_url:
        payload['avatar_url'] = avatar_url

    headers = {'Content-Type': 'application/json'}
    if thread_id:
        webhook_url = f'{webhook_url}?thread_id={thread_id}'
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        clear_screen()
        display_logo('Thread message posted successfully!'.center(121))
    else:
        clear_screen()
        display_logo(f'Failed to post thread message with status code: {response.status_code}'.center(121))
        

webhook_url = get_webhook_url()
webhook_name = get_webhook_name()
thread_id = get_thread_id()
avatar_url = get_avatar_url()
json_file_path = get_json_file_path()

post_thread_message(webhook_url, json_file_path, webhook_name, thread_id, avatar_url)

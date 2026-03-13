import os
import json


# Stellt sicher, dass der 'data' Ordner existiert
if not os.path.exists('data'):
    os.makedirs('data')


def write_to_textfile(user_id, username, user_data):
    filename_text = 'data/users.txt'
    try:
        with open(filename_text, 'a', encoding='utf-8') as t_file:
            name = user_data.get('name', '').capitalize()
            city = user_data.get('city', '').capitalize()
            age = user_data.get('age', '')
            line = f"@{username}| ID: {user_id} \nName: {name} | Age: {age} | City: {city}\n\n"
            t_file.write(line)
            print(f'Successfully added user "{username}" to {filename_text}')
    except Exception as e:
        print(f'Error writing to textfile: {e}')


def write_to_jsonfile(user_id, username, user_data):
    filename_json = 'data/users.json'
    
    # 1. Lese die bestehende Datei
    try:
        with open(filename_json, 'r', encoding='utf-8') as j_file:
            # Wenn die Datei leer ist, wird json.load einen Fehler werfen
            if os.path.getsize(filename_json) == 0:
                user_list = []
            else:
                user_list = json.load(j_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Wenn die Datei nicht existiert oder kaputt ist, starte mit einer leeren Liste
        user_list = []

    # 2. Füge den neuen User zur Liste hinzu
    new_entry = {
        "user_id": user_id,
        "username": username,
        "data": user_data
    }
    user_list.append(new_entry)

    # 3. Schreibe die komplette, aktualisierte Liste zurück
    try:
        with open(filename_json, 'w', encoding='utf-8') as j_file:
            # indent=4 sorgt für die schöne Formatierung
            json.dump(user_list, j_file, ensure_ascii=False, indent=4)
            print(f'Successfully updated {filename_json} with user "{username}"')
    except Exception as e:
        print(f'Error writing to jsonfile: {e}')


def save_user_data(user_id, username, user_data):
    """
    Hauptfunktion, um User-Daten sowohl als Text als auch als valides JSON zu speichern.
    """
    write_to_textfile(user_id, username, user_data)
    write_to_jsonfile(user_id, username, user_data)


def get_user_from_file(user_id):
    """
    Liest die valide JSON-Datei und sucht nach einem User anhand seiner ID.
    Gibt das User-Dictionary zurück, wenn gefunden, sonst None.
    """
    filename_json = 'data/users.json'
    try:
        if not os.path.exists(filename_json):
            return None
            
        with open(filename_json, 'r', encoding='utf-8') as file:
            # check if file is empty
            if os.path.getsize(filename_json) == 0:
                return None
                
            users = json.load(file)
            
            # Suche nach dem User
            for user in users:
                if user.get('user_id') == user_id:
                    return user
            
            return None
            
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

# ITA-Wiki API-Wrapper für Python
Das ist ein simpler API-Wrapper für das ITA-Wiki geschrieben in Python.

___

# Benutzung
```python
from itawiki_api_wrapper import auth, posts, categories, announcements

auth.login('EMAIL/NAME', 'PASSWORT')
```
___

# Auth

| Methode      | Beschreibung |
| ----------- | ----------- |
| login(username, password)      | Loggt sich mich den angegebenen Daten ein und speichert einen Token in einer Variable.       |
| logout()   | Meldet sich mit dem angemeldeten Benuzter ab.       |
| details()  | Zeigt einige Details vom angemeldeten Benutzer.  |

___

# Posts
| Methode | Beschreibung |
| ----------- | ----------- |
| search(keywords) | Sucht nach einem Post auf dem Wiki und gibt diesen in einem Dictionary wieder. |

___

# Categories
| Methode | Beschreibung |
| ----------- | ----------- |
| get_categories() | Gibt alle derzeitig vertretenen Kategorien aus. |

___

# Announcements
| Methode | Beschreibung |
| ----------- | ----------- |
| get_announcements() | Gibt alle Announcements aus. |

___

# Beispiel
```python
from itawiki_api_wrapper import auth, posts

auth.login('Mustermann', 'Secret123')

print(posts.search("Mathe"))

auth.logout()
```

# Output
```python
{'url': 'https://ita-wiki.de/posts/25', 'post_id': 25, 'title': 'Ausdrücke und mathematische Operatoren', 'created_at': '2021-10-29T19:22:15.000000Z'}
```

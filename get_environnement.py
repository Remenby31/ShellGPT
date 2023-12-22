import os
import platform

def get_system_type():
    """Renvoie le type de système d'exploitation."""
    try:
        return platform.linux_distribution()[0].lower()
    except AttributeError:
        return platform.system().lower()

def get_terminal():
    """Renvoie le type de terminal utilisé ou 'terminal' par défaut."""
    return os.environ.get('TERM', 'terminal')

def get_current_path():
    """Renvoie le chemin du répertoire courant."""
    return os.path.dirname(os.path.realpath(__file__))

def list_directory_contents(directory='.', limit=30):
    """Renvoie une liste des contenus du répertoire jusqu'à une limite spécifiée."""
    contents = os.listdir(directory)
    return contents[:limit]

def get_environnement():
    """Renvoie les détails de l'environnement du système."""
    system_type = get_system_type()
    terminal_type = get_terminal()
    current_path = get_current_path()
    directory_contents = list_directory_contents()

    return system_type, terminal_type, current_path, directory_contents

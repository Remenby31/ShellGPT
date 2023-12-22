import subprocess, os, sys
from get_environnement import get_environnement
from gpt_prompt import get_gpt_command, check_gpt_end

# Initialiser l'API OpenAI avec la clé d'API

def execute_command(command, historique):
    print(f"[GPT] {command}")
    
    _ , terminal_name, _, _ = get_environnement()

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if len(result.stdout) > 1:
            print(f"[{terminal_name}] {result.stdout[:-1]}")
        historique += '[terminal]' + result.stdout + '\n'

    except subprocess.CalledProcessError as e:
        print(f"[{terminal_name} - Erreur] {e.stderr}")
        historique += '[terminal]' + e.stderr + '\n'
    
    return historique

def main(task_description):
    task_in_progress = True
    historique = ''
    max_iter = 5 # Nombre d'itérations maximum

    while task_in_progress and max_iter > 0:
        # Obtenir la commande à exécuter
        historique, command = get_gpt_command(task_description, historique)
        if command:
            # Exécuter la commande
            historique = execute_command(command, historique)
            # Vérifier si la tâche est terminée
            task_in_progress = not check_gpt_end(historique, task_description)
        max_iter -= 1
    
    # Vérifier si le nombre d'itérations est dépassé
    if max_iter == 0:
        print("Trop d'itérations. Fin du programme.")

if __name__ == "__main__":
    # Vérifier si l'argument est fourni
    if len(sys.argv) < 2:
        print("Veuillez fournir une tâche à réaliser en argument.")
        sys.exit(1)

    # Exécuter la tâche
    main(sys.argv[1])

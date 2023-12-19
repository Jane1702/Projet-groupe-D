import subprocess
# ....


def get_current_commit_hash():
    # Obtenez le hachage du commit actuel
    return subprocess.check_output(["git", "rev-parse", "HEAD"], universal_newlines=True).strip()

def run_tests():
    # Exécutez vos tests ici. Assurez-vous d'ajuster la commande en fonction de votre projet.
    try:
        subprocess.check_output(["python", "tests.py"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True  # Les tests ont réussi
    except subprocess.CalledProcessError as e:
        print(f"Les tests ont échoué:\n{e.output}")
        return False  # Les tests ont échoué
def push_to_dev_branch():
    # Poussez la branche actuelle vers la branche "dev"
    subprocess.run(["git", "push", "origin", "HEAD:dev"])

def advance_dev_branch():
    # Poussez la branche "dev" vers l'amont (avancez d'un commit)
    subprocess.run(["git", "push", "origin", "dev"])

def main():
    # Exécutez les tests
    if not run_tests():
        print("Les tests ont échoué. Création de la branche de défaillance et push sur la branche dev.")
        
        # Obtenez le numéro de commit
        commit_hash = get_current_commit_hash()

        # Créez une branche de défaillance avec le numéro de commit
        create_failure_branch(commit_hash)

        # Poussez la branche de défaillance sur la branche dev
        push_to_dev_branch()
    else:
        print("Les tests ont réussi. Avancement de la branche dev.")
        advance_dev_branch()

if __name__ == "__main__":
    main()
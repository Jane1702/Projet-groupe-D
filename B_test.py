import subprocess

def run_tests():
    # Exécutez vos tests ici. Assurez-vous d'ajuster la commande en fonction de votre projet.
    try:
        subprocess.check_output(["python", "tests.py"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True  # Les tests ont réussi
    except subprocess.CalledProcessError as e:
        print(f"Les tests ont échoué:\n{e.output}")
        return False  # Les tests ont échoué

def create_failure_branch():
    # Générez un nom de branche unique pour la branche de défaillance
    failure_branch_name = "failure_branch"

    # Créez une nouvelle branche
    subprocess.run(["git", "checkout", "-b", failure_branch_name])

def push_to_dev_branch():
    # Poussez la branche actuelle vers la branche "dev"
    subprocess.run(["git", "push", "origin", "HEAD:dev"])

def main():
    # Exécutez les tests
    if not run_tests():
        print("Les tests ont échoué. Création de la branche de défaillance et push sur la branche dev.")
        
        # Créez une branche de défaillance
        create_failure_branch()

        # Poussez la branche de défaillance sur la branche dev
        push_to_dev_branch()
    else:
        print("Les tests ont réussi. Aucune action nécessaire.")

if __name__ == "__main__":
    main()
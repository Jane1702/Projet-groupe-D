import git
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
    repo_path = "C:/Users/Thuy-trang/Desktop/Projet-groupe-D"  # Remplacez par le chemin de votre repo
    repo = git.Repo(repo_path)

    # Assurez-vous que la branche "failure" n'existe pas déjà
    if "failure" in repo.branches:
        print("La branche 'failure' existe déjà.")
        return

    # Créez la nouvelle branche si les tests ont échoué
    if not run_tests():
        current_branch = repo.active_branch
        new_branch = repo.create_head("failure", commit=current_branch.commit)

        # Passez à la nouvelle branche
        repo.head.reference = new_branch
        repo.head.reset(index=True, working_tree=True)

        print("La branche 'failure' a été créée avec succès.")

if __name__ == "__main__":
    create_failure_branch()
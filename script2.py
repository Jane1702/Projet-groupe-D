import subprocess
import datetime


def pull_dev_branch():
    # Pull changes from the dev branch
    subprocess.run(["git", "pull", "origin", "dev"])


def run_tests():
    # Run your tests here. Adjust the command based on your project.
    try:
        subprocess.check_output(
            ["python", "tests.py"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        return True  # Tests passed
    except subprocess.CalledProcessError as e:
        print(f"Tests failed:\n{e.output}")
        return False  # Tests failed


def create_failure_branch():
    # Generate a unique name for the failure branch using timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    failure_branch_name = f"failures/{timestamp}"

    # Commit the changes before creating the failure branch
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Commit before failure branch creation"])

    # Check if the failure branch already exists
    existing_branch_check = subprocess.run(
        ["git", "rev-parse", "--verify", failure_branch_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    if existing_branch_check.returncode != 0:
        # Create a new failure branch
        subprocess.run(["git", "checkout", "-b", failure_branch_name])
    else:
        # Switch to the existing failure branch
        subprocess.run(["git", "checkout", failure_branch_name])


def fast_forward_to_main():
    # Fast-forward the dev branch to main
<<<<<<< HEAD
    subprocess.run(["git", "checkout", "master"])
=======
    subprocess.run(["git", "checkout", "main"])
>>>>>>> a3dbb63e26a37548c40155f40acb175e25806e83
    subprocess.run(["git", "merge", "dev", "--ff-only"])


def push_to_dev_branch():
    # Push the current branch to the dev branch
    subprocess.run(["git", "push", "origin", "HEAD:dev"])


def main():
    # Pull changes from the dev branch
    pull_dev_branch()

    # Run tests
    if not run_tests():
        print(
            "Tests failed. Creating the failure branch and pushing to the dev branch."
        )

        # Create or switch to the failure branch
        create_failure_branch()

        # Push the failure branch to the dev branch
        push_to_dev_branch()
    else:
        print("Tests passed. Fast-forwarding to main and pushing changes.")

        # Fast-forward the dev branch to main
        fast_forward_to_main()

        # Push changes to the dev branch
        push_to_dev_branch()


if __name__ == "__main__":
    main()

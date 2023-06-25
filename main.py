import os
import subprocess
import shutil

# Function to clone a repository
def clone_repository(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url])
        return True
    except Exception as e:
        print(f"Error: Failed to clone repository - {str(e)}")
        return False

# Function to merge branches
def merge_branch(repo_path, branch_name):
    try:
        os.chdir(repo_path)
        subprocess.run(['git', 'checkout', 'main'])
        subprocess.run(['git', 'pull'])
        subprocess.run(['git', 'merge', branch_name])
        return True
    except Exception as e:
        print(f"Error: Failed to merge branch - {str(e)}")
        return False

# Function to push changes to a new repository
def push_to_new_repository(repo_path, new_repo_url):
    try:
        subprocess.run(['git', 'remote', 'set-url', 'origin', new_repo_url])
        subprocess.run(['git', 'push', '-u', 'origin', 'main'])
        return True
    except Exception as e:
        print(f"Error: Failed to push changes to new repository - {str(e)}")
        return False

# Main script
if __name__ == "__main__":
    # Get user input for the GitHub repository link
    repo_link = input("Enter the GitHub repository link: ")

    # Clone the repository
    if clone_repository(repo_link):
        repo_name = repo_link.split('/')[-1].split('.')[0]
        repo_path = os.path.join(os.getcwd(), repo_name)

        # Get user input for the branch to merge
        branch_name = input("Enter the branch name to merge: ")

        # Merge the branch
        if merge_branch(repo_path, branch_name):
            # Get user input for the new repository link
            new_repo_link = input("Enter the new repository link to push the changes: ")

            # Push changes to new repository
            if push_to_new_repository(repo_path, new_repo_link):
                print("Merging and pushing changes completed successfully.")
            else:
                print("Failed to push changes to new repository.")
        else:
            print("Failed to merge branch.")
    else:
        print("Failed to clone repository.")
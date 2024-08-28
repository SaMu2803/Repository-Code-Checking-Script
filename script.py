from pymoss import Moss

def check_plagiarism_moss(repository_path):
    moss = Moss('YOUR_MOSS_USER_ID', 'python')  # Replace 'python' with the appropriate language
    moss.set_ignore_limit(10)  # Set limit for ignoring small similarities
    
    # Add files from the repository for comparison
    import os
    for root, _, files in os.walk(repository_path):
        for file_name in files:
            if file_name.endswith('.py'):  # Example for Python files; change based on your use case
                moss.add_file(os.path.join(root, file_name))

    # Send files to MOSS server
    result_url = moss.send()
    print(f"Plagiarism check results available at: {result_url}")

repository_path = "/path/to/your/repository"
check_plagiarism_moss(repository_path)

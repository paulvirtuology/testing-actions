import os

def main():
    # Get branch name from the environment variable or default
    branch_name = os.getenv("BRANCH_NAME", "unknown")
    
    if branch_name == "dev":
        message = "This is from dev branch\n"
    elif branch_name == "main":
        message = "This is from main branch\n"
    else:
        message = f"This is from {branch_name} branch\n"
    
    # Write the message to the output file
    with open("output.log", "w") as f:
        f.write(message)
    
    print(f"Message written: {message}")

if __name__ == "__main__":
    main()

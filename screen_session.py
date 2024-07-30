import subprocess
import os
def create_screen_session(session_name,script_path):
    try:
        if not os.path.isfile(script_path):
            print(f"the script {script_path} does not exist.")
            return
        subprocess.run(['screen','-S',session_name, '-dm'], check=True)
        result = subprocess.run(['screen', '-ls'],capture_output=True,text=True)
        if session_name in result.stdout:

            print(f"screen session '{session_name}'creaded successfully.")
        else:
            print(f"screen session '{session_name}'not found after creation.")
            return
        run_command = f'python3 {script_path}'

        subprocess.run(['screen','-S',session_name,'-X','stuff',run_command + '\n'], check=True)
        print(f"the scrpt '{script_path}' is being executed in session '{session_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    sessions = {
            "hello_world_session":"hello.py",
            "hello_session":"test.py"
            }
    for session_name,script_path in sessions.items():
        create_screen_session(session_name,script_path)


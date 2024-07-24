import subprocess
import argparse
import datetime
import os

def run_ffuf(target, wordlist, ffuf_path):

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    sanitized_target = target.replace('http://', '').replace('https://', '').replace('/', '_').replace(':', '_')
    output_file = f'{sanitized_target}_{timestamp}.txt'
    
    command = [
        ffuf_path,  # Using the specified path to ffuf
        '-u', f'{target}/FUZZ',
        '-w', wordlist,
        '-v'
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        with open(output_file, 'w') as outfile:
            outfile.write(result.stdout)
        print(f"Ffuf scan completed successfully. Results saved to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running ffuf: {e}")
        with open('ffuf_error.log', 'w') as errorfile:
            errorfile.write("Command: " + ' '.join(command) + '\n')
            errorfile.write("Return code: " + str(e.returncode) + '\n')
            errorfile.write("stdout: " + e.stdout + '\n')
            errorfile.write("stderr: " + e.stderr + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run ffuf to fuzz a target URL.')
    parser.add_argument('target', help='The target URL to fuzz')
    parser.add_argument('--ffuf_path', default='C:\\Users\\Yash\\Desktop\\fuff\\ffuf.exe', help='The path to the ffuf executable')
    args = parser.parse_args()

    target = args.target
    wordlist = 'common.txt'
    ffuf_path = args.ffuf_path
    run_ffuf(target, wordlist, ffuf_path)

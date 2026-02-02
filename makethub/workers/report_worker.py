import subprocess

def submit_report(text):
    subprocess.Popen(f"echo {text} >> /tmp/reports.txt", shell=True)
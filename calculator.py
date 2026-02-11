HISTORY_FILE="history.txt"
def show_history():
    file=open(HISTORY_FILE,"r")
    lines=file.readlines()
    if len(lines)==0:
        print("no history")
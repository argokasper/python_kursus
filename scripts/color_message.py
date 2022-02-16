class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m' # sinine
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m' # roheline
    WARNING = '\033[93m' # kollane
    FAIL = '\033[91m' # punane
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# f"{bcolors.WARNING}See on hoiatus!{bcolors.ENDC}"

# levels: INFO=sinine, SUCCESS=roheline, WARNING=kollane, DANGER=punane
def report_status(message: str, level = "INFO"):
    color = ""
    if level == "INFO":
        color = bcolors.OKBLUE
    elif level == "SUCCESS":
        color = bcolors.OKGREEN
    elif level == "WARNING":
        color = bcolors.WARNING
    elif level == "DANGER":
        color = bcolors.FAIL

    return f"{color}{message}{bcolors.ENDC}"


print(report_status("See on test"))
print(report_status("Kõik on OK", "SUCCESS"))
print(report_status("See on hoiatus", "WARNING"))
print(report_status("See on error", "DANGER"))
print(report_status("See on üllatus", "DEBUG"))

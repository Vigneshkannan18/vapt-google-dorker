#!/usr/bin/env python3

import webbrowser
import urllib.parse
import time
import json
from pathlib import Path


# ============================================================
# 75 GOOGLE DORKS FOR AUTHORIZED WEB VAPT
# ============================================================

def generate_dorks(domain):

    domain = domain.strip()
    domain = domain.replace("https://", "")
    domain = domain.replace("http://", "")
    domain = domain.rstrip("/")

    dorks = [

        # ====================================================
        # 1-20 : FILES / DOCUMENTS / BACKUPS
        # ====================================================

        f"site:{domain}",
        f"site:{domain} filetype:pdf",
        f"site:{domain} filetype:doc",
        f"site:{domain} filetype:docx",
        f"site:{domain} filetype:xls",
        f"site:{domain} filetype:xlsx",
        f"site:{domain} filetype:csv",
        f"site:{domain} filetype:txt",
        f"site:{domain} filetype:xml",
        f"site:{domain} filetype:json",
        f"site:{domain} filetype:sql",
        f"site:{domain} filetype:log",
        f"site:{domain} filetype:conf",
        f"site:{domain} filetype:config",
        f"site:{domain} filetype:ini",
        f"site:{domain} filetype:env",
        f"site:{domain} filetype:bak",
        f"site:{domain} filetype:old",
        f"site:{domain} filetype:zip",
        f"site:{domain} filetype:tar",

        # ====================================================
        # 21-25 : DIRECTORY LISTING
        # ====================================================

        f"site:{domain} intitle:\"index of\"",
        f"site:{domain} intitle:\"index of\" backup",
        f"site:{domain} intitle:\"index of\" files",
        f"site:{domain} intitle:\"index of\" documents",
        f"site:{domain} intitle:\"index of\" uploads",

        # ====================================================
        # 26-35 : ADMIN / AUTH / FILE HANDLING
        # ====================================================

        f"site:{domain} inurl:admin",
        f"site:{domain} inurl:administrator",
        f"site:{domain} inurl:login",
        f"site:{domain} inurl:portal",
        f"site:{domain} inurl:dashboard",
        f"site:{domain} inurl:backup",
        f"site:{domain} inurl:backups",
        f"site:{domain} inurl:upload",
        f"site:{domain} inurl:uploads",
        f"site:{domain} inurl:download",

        # ====================================================
        # 36-40 : API / DOCUMENTATION
        # ====================================================

        f"site:{domain} inurl:api",
        f"site:{domain} inurl:swagger",
        f"site:{domain} inurl:graphql",
        f"site:{domain} inurl:docs",
        f"site:{domain} inurl:documentation",

        # ====================================================
        # 41-50 : INFORMATION DISCLOSURE
        # ====================================================

        f"site:{domain} \"confidential\"",
        f"site:{domain} \"internal use only\"",
        f"site:{domain} \"password\"",
        f"site:{domain} \"username\"",
        f"site:{domain} \"api key\"",
        f"site:{domain} \"database\"",
        f"site:{domain} \"backup\"",
        f"site:{domain} \"configuration\"",
        f"site:{domain} \"stack trace\"",
        f"site:{domain} \"error\"",

        # ====================================================
        # 51-55 : SOURCE / DEVELOPMENT FILES
        # ====================================================

        f"site:{domain} filetype:map",
        f"site:{domain} filetype:js",
        f"site:{domain} filetype:php",
        f"site:{domain} filetype:asp",
        f"site:{domain} filetype:aspx",

        # ====================================================
        # 56-60 : DEVELOPMENT / REPOSITORY EXPOSURE
        # ====================================================

        f"site:{domain} inurl:.git",
        f"site:{domain} inurl:.svn",
        f"site:{domain} \"package.json\"",
        f"site:{domain} \"docker-compose\"",
        f"site:{domain} \"Jenkinsfile\"",

        # ====================================================
        # 61-65 : DEBUG / ERROR / DEVELOPMENT
        # ====================================================

        f"site:{domain} \"debug\"",
        f"site:{domain} \"debug mode\"",
        f"site:{domain} \"exception\"",
        f"site:{domain} \"traceback\"",
        f"site:{domain} \"PHP Version\"",

        # ====================================================
        # 66-70 : TEMP / BACKUP / CONFIG FILES
        # ====================================================

        f"site:{domain} filetype:tmp",
        f"site:{domain} filetype:temp",
        f"site:{domain} filetype:orig",
        f"site:{domain} filetype:swp",
        f"site:{domain} filetype:save",

        # ====================================================
        # 71-75 : SECURITY / INTERNAL / CLOUD
        # ====================================================

        f"site:{domain} \"security.txt\"",
        f"site:{domain} \"robots.txt\"",
        f"site:{domain} \"sitemap.xml\"",
        f"site:{domain} \"internal\"",
        f"site:{domain} \"staging\"",
    ]

    return dorks


# ============================================================
# GOOGLE URL
# ============================================================

def google_url(dork):

    encoded = urllib.parse.quote_plus(dork)

    return f"https://www.google.com/search?q={encoded}"


# ============================================================
# SESSION FILE
# ============================================================

def session_file(domain):

    safe_domain = domain.replace(".", "_").replace("/", "_")

    return Path(f"google_dork_session_{safe_domain}.json")


def load_session(domain):

    file = session_file(domain)

    if file.exists():

        try:

            with open(file, "r") as f:

                data = json.load(f)

            return set(data.get("opened", []))

        except:

            return set()

    return set()


def save_session(domain, opened):

    file = session_file(domain)

    data = {
        "domain": domain,
        "opened": sorted(list(opened))
    }

    with open(file, "w") as f:

        json.dump(data, f, indent=4)


# ============================================================
# SHOW ALL DORKS
# ============================================================

def show_dorks(dorks, opened):

    print("\n" + "=" * 75)
    print("GOOGLE DORKS")
    print("=" * 75)

    for i, dork in enumerate(dorks, start=1):

        if i in opened:

            status = "[OPENED]"

        else:

            status = "[NEW]   "

        print(f"{i:02d}. {status} {dork}")

    print("=" * 75)


# ============================================================
# OPEN SELECTED DORKS
# ============================================================

def open_dorks(domain, dorks, opened, indices):

    new_indices = []

    for index in indices:

        if index < 1 or index > len(dorks):

            continue

        if index in opened:

            continue

        new_indices.append(index)

    if not new_indices:

        print("\nNo new dorks selected.")

        return

    print("\nOpening dorks...\n")

    for index in new_indices:

        dork = dorks[index - 1]

        print(f"Opening [{index}] {dork}")

        webbrowser.open_new_tab(
            google_url(dork)
        )

        opened.add(index)

        # Save progress immediately
        save_session(domain, opened)

        time.sleep(1)

    print("\nDone.")
    print(f"Opened: {len(new_indices)} dorks")


# ============================================================
# OPEN NEXT N DORKS
# ============================================================

def open_next(domain, dorks, opened):

    remaining = [
        i for i in range(1, len(dorks) + 1)
        if i not in opened
    ]

    if not remaining:

        print("\nAll 75 dorks have already been opened.")

        return

    try:

        amount = int(
            input("\nHow many dorks do you want to open? ")
        )

        if amount <= 0:

            print("Enter a number greater than 0.")

            return

    except ValueError:

        print("Please enter a number.")

        return

    selected = remaining[:amount]

    open_dorks(
        domain,
        dorks,
        opened,
        selected
    )


# ============================================================
# OPEN SPECIFIC DORKS
# ============================================================

def open_specific(domain, dorks, opened):

    print("\nExample:")
    print("7,11,17,21,26")
    print("or")
    print("51,52,53,60,75")

    user_input = input(
        "\nEnter dork numbers: "
    ).strip()

    if not user_input:

        return

    try:

        numbers = []

        for item in user_input.split(","):

            number = int(item.strip())

            if number not in numbers:

                numbers.append(number)

        open_dorks(
            domain,
            dorks,
            opened,
            numbers
        )

    except ValueError:

        print("\nInvalid input.")


# ============================================================
# SHOW REMAINING
# ============================================================

def show_remaining(dorks, opened):

    remaining = [
        i for i in range(1, len(dorks) + 1)
        if i not in opened
    ]

    print("\n" + "=" * 75)

    print(
        f"REMAINING DORKS: {len(remaining)}"
    )

    print("=" * 75)

    for i in remaining:

        print(
            f"{i:02d}. {dorks[i - 1]}"
        )

    print("=" * 75)


# ============================================================
# RESET PROGRESS
# ============================================================

def reset_session(domain):

    file = session_file(domain)

    confirm = input(
        "\nAre you sure you want to reset progress? (y/n): "
    ).lower()

    if confirm == "y":

        if file.exists():

            file.unlink()

        print("Progress reset.")

    else:

        print("Reset cancelled.")


# ============================================================
# MAIN MENU
# ============================================================

def menu(domain, dorks, opened):

    while True:

        total = len(dorks)

        opened_count = len(opened)

        remaining = total - opened_count

        print("\n")

        print("=" * 75)
        print("             GOOGLE DORKER - VAPT")
        print("=" * 75)

        print(f"Domain    : {domain}")
        print(f"Total     : {total}")
        print(f"Opened    : {opened_count}")
        print(f"Remaining : {remaining}")

        print("=" * 75)

        print("1. Open next N dorks")
        print("2. Open specific dorks")
        print("3. Show all dorks")
        print("4. Show remaining dorks")
        print("5. Reset progress")
        print("6. Exit")

        print("=" * 75)

        choice = input(
            "Choose option: "
        ).strip()

        if choice == "1":

            open_next(
                domain,
                dorks,
                opened
            )

        elif choice == "2":

            open_specific(
                domain,
                dorks,
                opened
            )

        elif choice == "3":

            show_dorks(
                dorks,
                opened
            )

        elif choice == "4":

            show_remaining(
                dorks,
                opened
            )

        elif choice == "5":

            reset_session(domain)

            opened.clear()

        elif choice == "6":

            save_session(
                domain,
                opened
            )

            print("\nProgress saved.")
            print("Exiting...")

            break

        else:

            print("\nInvalid option.")


# ============================================================
# PROGRAM START
# ============================================================

def main():

    print("=" * 75)
    print("             GOOGLE DORKER - VAPT")
    print("             75 DORKS")
    print("=" * 75)

    domain = input(
        "\nEnter target domain: "
    ).strip()

    if not domain:

        print("Domain cannot be empty.")

        return

    domain = domain.replace(
        "https://", ""
    )

    domain = domain.replace(
        "http://", ""
    )

    domain = domain.rstrip("/")

    dorks = generate_dorks(domain)

    opened = load_session(domain)

    print(
        f"\n{len(dorks)} VAPT dorks generated."
    )

    if opened:

        print(
            f"Previous progress found: "
            f"{len(opened)} dorks already opened."
        )

    else:

        print("Starting new session.")

    menu(
        domain,
        dorks,
        opened
    )


if __name__ == "__main__":

    main()

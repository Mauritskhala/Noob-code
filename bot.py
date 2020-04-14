# 宋瑞雨 10175300208

from time import sleep
from termcolor import colored
from simpleeval import simple_eval
import random



class Bot:

    wait = 0

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'cyan')

    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _warn(self, s):
        return colored(s, 'red')


class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"

    def _think(self, s):
        return f"Hello {s}"


class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"

    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too."
        else:
            return "Sorry to hear that."


class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow',
                  'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"


class CalcBot(Bot):
    def __init__(self):
        self.q = "Through recent upgrade I can do calculation now. If you want stop calculation,please enter 'q' or 'x' or 'quit'.\nInput some arithmetic expression to try:"
        self.q2 = "You can continue to input now. If you want stop calculation,please enter 'q' or 'x' or 'quit'.\nInput some arithmetic expression to try:"
        self.te = "ok,I will stop now. We can talk about something else."
        self.warn = "Oh, that looks like something else. You should give me a right expression."

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"

    def run(self):
        cal_flag = True
        while cal_flag:
            sleep(Bot.wait)
            print(self._format(self.q))
            self.q = self.q2
            self.a = input()
            cal_flag = not (self.a == 'q' or self.a == 'x' or self.a == 'quit')
            if cal_flag == False:
                sleep(Bot.wait)
                print(self._format(self.te))
                break
            sleep(Bot.wait)
            try:
                print(self._format(self._think(self.a)))
            except:
                print(self._warn(self.warn))

    def _warn(self, calwarning):
        return colored(calwarning, 'red')


class FingerGuessing(Bot):

    def __init__(self):
        self.q = "I like playing games.Let's play finger guessing. You can use number '1','2','3' standing for Scissors,rock,paper.Enter 'q' to quit."
        self.figure = {'1': 'Scissors', '2': 'rock', '3': 'paper'}
        self.warn = "Please don't cheat :(,I don't know what you mean."

    def _think(self, s):
        choice = random.randint(1, 3)
        checkpoint = int(s) - choice
        if checkpoint == 1 or checkpoint == -2:
            result = "win"
        elif checkpoint == 0:
            result = 'draw'
        else:
            result = 'lose'
        choice = str(choice)
        return f"You showed {self.figure[s]},I showed {self.figure[choice]}, You {result}."

    def run(self):
        while True:
             sleep(Bot.wait)
             print(self._format(self.q))
             self.q = "Let's continue.Enter q to quit"
             self.a = input()
             if self.a == 'q':
                break
             try:
                sleep(Bot.wait)
                print(self._format(self._think(self.a)))
             except:
                print(self._warn(self.warn))


class CyberFriend:

    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt(colored("This is Cyberex dialog system. Let's talk.",'cyan'))
        for bot in self.bots:
            bot.run()

    def choose_to_run(self):
        try:
            choice = int(input(colored("Please enter the number of topic you want to talk:\n1.greetings 2.favourite color 3.calculation 4.finger guessing\n",'cyan')))
            self.bots[choice].run()
        except:
            print(colored("What are you saying ?",'red'))


Cyberex = CyberFriend(1)
Cyberex.add(HelloBot())
Cyberex.add(GreetingBot())
Cyberex.add(FavoriteColorBot())
Cyberex.add(CalcBot())
Cyberex.add(FingerGuessing())
mode = input(colored(
    "Auto run bot or run depending on your request?(1 for auto run and else for free choice)\n",'cyan'))
if mode == '1':
    Cyberex.run()
else:
    Cyberex.choose_to_run()

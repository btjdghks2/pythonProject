# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # print('47')
    # start = 'Na' * 4 + '\n'
    # middle = 'Hey' * 3 + '\n'
    # end = 'Goodbye.'
    # print(start + start + middle + end)
    # print('exam!')
    # crypto_list = ['Yeti','Bigfoot','Loch Ness Monster']
    # crypto_string = ','.join(crypto_list)
    # print('Found and signing book deals:', crypto_string)
    # count = 1
    # while count <= 5:
    #     print(count)
    #     count += 1
    #
    # while True:
    #     stuff = input("String to capitalize [type q to quit]: ")
    #     if stuff =='q':
    #         break
    #         print(stuff.capitalize())
    # while True:
    #     value = input("Integer,please[q to quit]:")
    #     if value == 'q': # 종료
    #         break
    #         number = int(value)
    #         if number % 2 == 0: # 짝수
    #             countine
    #             print(number,"squared is", number*number)
    #
    #     for x in range(0,3):
    #         print(x)

# one_marx = 'Groucho',
# type(one_marx)
# type('Groucho')
#
# marx_tuple = ('Groucho','Chico','Harpo')
# a,b,c = marx_tuple
#
# marx_list = ['Groucho','Chico','Harpo']
# tuple(marx_list)
#
# list(marx_tuple)
# print(marx_tuple)
#
# print(marx_tuple[0])
# print(marx_tuple[1])
# print(marx_tuple[2])
# print(marx_tuple[::-1])
# marx_list.append('Zeppo')
# print(marx_list)
# marx_list.insert(2,'Gummo')
# print(marx_list)
# print(marx_list[2] * 3)
# numbers = [1,2,3,4]
# numbers[1:3] = ['atp','bbt']
# print(numbers)
# del numbers[-1]
# print(numbers)
# numbers.pop()
# numbers.pop()
# print(numbers.pop())
#
#
#
# a = [1,2,3]
# b = a.copy()
# c = list(a)
# d = a[:]
# print(a)
# print(b)
# print(c)
# print(d)
# a[0] = 'side'
# print(a,b,c,d)

empty_dict = {}


empty_dict = {"day": "A period of twenty-four hours, mostly misspent",
              "positive": "Mistaken at the top of ine's voice",
              "misfortune": "The kind of fortune that never misses",}

print(empty_dict)

acme_customer = {'first': 'Wile', 'middle':'E', 'last': 'Coyote'}
print(acme_customer)
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

lol = [['a','b'],['c','d'],['e','f']]
dict(lol)
{'a':'b','c':'d','e':'f'}
print(lol)

some_pythons = {
    'Graham':'Chapman',
    'John':'Cleese',
    'Eric':'Idle',
    'Terry':'Gilliam',
    'Michael':'Palin',
    'Terry':'Jones',
}
print(some_pythons.get('John'))
print(some_pythons.get('John','Not a Python'))

print(list(some_pythons.keys()))
print(len(some_pythons))

first = {'a':'agony', 'b':'bliss'}
second = {'b':'bagels','c':'candy'}
print({**first,**second})
third = {'d': 'donuts'}
print({**first,**third,**second})
others = {'Marx': 'Groucho','Howrd':'Moe'}
some_pythons.update(others)
print(some_pythons)

del some_pythons['Marx']
print(some_pythons)
print(len(some_pythons))
print(some_pythons.pop('John'))
some_pythons.pop('first','Hugo')
print('Graham' in some_pythons)
signals = {'green': 'go', 'yellow':'go faster','red':'smile for hte camera'}
save_signals = signals

print(save_signals)
original_signls = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signls)
signals = {'green': 'go', 'yellow':'go faster','red': ['stop','smile']}
print(signals)
signals['red'][1]='sweat'
print(signals)
signals_copy = signals.copy()
print(signals_copy)

signals_copy = copy.deepcopy(signals)

print(signals)

signals['red'][1]= 'sweat'

print(signals_copy)

print("Linux update!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

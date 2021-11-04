# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

one_marx = 'Groucho',
type(one_marx)
type('Groucho')

marx_tuple = ('Groucho','Chico','Harpo')
a,b,c = marx_tuple

marx_list = ['Groucho','Chico','Harpo']
tuple(marx_list)

list(marx_tuple)
print(marx_tuple)

print(marx_tuple[0])
print(marx_tuple[1])
print(marx_tuple[2])
print(marx_tuple[::-1])
marx_list.append('Zeppo')
print(marx_list)
marx_list.insert(2,'Gummo')
print(marx_list)
print(marx_list[2] * 3)
numbers = [1,2,3,4]
numbers[1:3] = ['atp','bbt']
print(numbers)
del numbers[-1]
print(numbers)
numbers.pop()
numbers.pop()
print(numbers.pop())



a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
a[0] = 'side'
print(a,b,c,d)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

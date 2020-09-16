import sys
import time

data = sys.stdin.readline()
data = 'test'

for i in range(5):
    print('Hello, ', i, '?')

time.sleep(1)
print('Hello, ' + data + '!')
time.sleep(2)
print('Hello, ' + data + '!!')
time.sleep(1)
print('Hello, ' + data + '!!!')
time.sleep(1)
print('Hello, ' + data + '!!!!')
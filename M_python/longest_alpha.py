n = 0
place_buffer = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_buffer = []
save_buffer = []
string_print = ""

s = input("Enter letters:")

for char in s:
    for i in range(26):
        if alphabet[i] == char:
         place_buffer.append(str(i))

while n < (len(place_buffer)-1):
   
    alpha_buffer.append(place_buffer[n])
    while n < (len(place_buffer)-1) and int(place_buffer[n]) <= int(place_buffer[n+1]):
        alpha_buffer.append(place_buffer[n+1])
        n = n + 1
   
    
    if (len(save_buffer) == 0) or (len(alpha_buffer) > len(save_buffer[0])):
        save_buffer = []
        save_buffer.append(alpha_buffer)
    
    n = n + 1
    alpha_buffer = []

for item in save_buffer:
    for i in item:
        string_print += alphabet[int(i)]
    
print(string_print)
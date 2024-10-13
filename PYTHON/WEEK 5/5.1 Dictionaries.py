d={}
d['samar']=7061262898
d['ahmad']=7856881973
d['sahil']=6207338743
print(d,type(d))

print(d['sahil'])



s = ['it', 'was', 'monday', 'morning', 'it', 'was']
max_count = 0
d = {}
ans = ''

for x in s:
    if x not in d:
        d[x] = 0  # Initialize the count for new words
    d[x] += 1  # Increment the count for the current word
    if d[x] > max_count:
        max_count = d[x]  # Update max_count if the current count is higher
        ans = x  # Update the word with the maximum count

print(ans)  # Print the word with the maximum count

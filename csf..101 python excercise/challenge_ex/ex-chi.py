with open('fruit_transactions.txt', 'r') as file:
    # File operations here
    content = file.read()
    print(content)
# File is automatically closed outside the with block

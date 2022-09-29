def user_system(string, users):
    store = string.split(' ')
    if store[0] == 'register':
        n = len(store[1])
        username = store[1][1:n-1]
        if username in users:
            return 'Username already exists'
        else:
            return 'Register successful'

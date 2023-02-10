def is_called():
    def is_returned():
        print('Hello')
    return is_returned


print(is_called())
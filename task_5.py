class NotNumException(Exception):
    def __init__(self, *args):
        if args:
            self.error_text = args[0]
        else:
            self.error_text = None

    def __str__(self):
        if self.error_text:
            return f"NotNumException: {self.error_text}"
        else:
            return "NotNumException!"


my_list = []
while True:
    user_input = input("Enter next number, or 'stop' to exit: ")
    if user_input == "stop":
        break
    try:
        if not user_input.isdigit():
            raise NotNumException(f"'{user_input}' has not numerical format")
        my_list.append(int(user_input))
    except NotNumException as e:
        print(e)

print(my_list)

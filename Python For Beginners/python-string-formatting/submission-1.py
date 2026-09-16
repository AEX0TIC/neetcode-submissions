def say_goodbye(name: str, hour: int) -> str:
    say_goodbye = "Goodbye, {}. See you again at {} o'clock.".format(name, hour)
    return say_goodbye


# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))

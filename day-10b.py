import time

print(time.time())


def send_emails():
    for n in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()

duration = end - start
print("duration: ", duration)

class word:
    def write(message):
        print("")
        for word in message:
            time.sleep(0.07)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
    def write2(message):
        for word in message:
            time.sleep(0.07)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""

while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  
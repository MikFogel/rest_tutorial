class A:

    def __init__(self):
        self.data = "hello"

    def __str__(self):
        return self.data


class B:

    def __init__(self):
        self.data = "bye"

    def __str__(self):
        return self.data


holder = []


for i in range(10):

    if i < 5:
        holder.append(A())
    else:
        holder.append(B())






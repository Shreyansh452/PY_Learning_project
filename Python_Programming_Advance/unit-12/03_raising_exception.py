from re import A


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is now right - shreyansh")
a = increment('s3fh3d')
print(a)
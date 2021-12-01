#!/usr/bin/env python3
# this wizard automatically creates a file for day X
# with boilerplate code
import os
import stat


BOILERPLATE = """
#!/usr/bin/env python3
import os


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")
""".strip()


if __name__ == '__main__':
    filename = input("Enter the day, typically 'day1' or 'day4': ")
    py_filename = filename + '.py'
    with open(py_filename, 'w+') as f:
        f.write(BOILERPLATE)

    st = os.stat(py_filename)
    os.chmod(py_filename, st.st_mode | stat.S_IEXEC)

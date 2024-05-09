import cProfile
import pstats
import io
import os

def say(function):
    print(f'Profiling: {function} \n')
    pr = cProfile.Profile()
    pr.enable()
    exec(function)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    files = get_files()
    ps.print_stats()
    string = s.getvalue().split('\n')[0] + '\n'
    string += s.getvalue().split('\n')[4] + '\n'


    for line in s.getvalue().split('\n'):
        if line:
            if any(file in line for file in files):
              string += line + '\n'
    string = filter(string)
    print(string)

def get_files():
    files =[]
    current_dir = os.path.dirname(os.path.realpath(__file__))
    for dirpath, dirnames, filenames in os.walk(current_dir):
        dirnames[:] = [d for d in dirnames if d not in ['.venv', '.conda']]
        for file in filenames:
            if file.endswith('.py'):
                files.append(os.path.join(dirpath, file))
    return files

def filter(string):
    lines = string.split('\n')
    new_lines = []
    for line in lines:
        if not '<module>' in line:
            new_lines.append(line)
    return '\n'.join(new_lines)

if __name__ == '__main__':
    function= "import main; main.run()"
   
    say(function)

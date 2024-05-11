import cProfile
import pstats
import io
import os
import time
def say(function):
    print(f'Profiling: {function} \n')
    pr = cProfile.Profile()
    pr.enable()
    start_time = time.time()    
    exec(function)
    end_time = time.time()
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
    # string = filter(string)
    print(string)
    print(f'Execution time: {end_time - start_time} seconds')

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


def mark(start=None, label='initial'):
    if start:
        execution_time = time.time() - start
        if execution_time > 1:
            print(f'{label}: {execution_time} seconds')
    return time.time()

if __name__ == '__main__':
    function= "import main; main.run()"
   
    say(function)

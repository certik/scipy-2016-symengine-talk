import matplotlib.pyplot as plt
import json
import numpy as np

def generate_images():
    with open('data.json', 'r') as f:
        tests = json.loads(f.read())
    for test in tests:
        name = test[0]
        param = np.log(test[1][:])
        plt.plot(param, np.log(test[2]), 'g', label="SymEngine")
        plt.plot(param, np.log(test[3]), 'b', label="GiNaC")
        plt.plot(param, np.log(test[4]), 'r', label="Mathematica")
        plt.plot(param, np.log(test[5]), 'y', label="SymPy")
        plt.plot(param, np.log(test[6]), 'c', label="Maple")
        plt.xlabel('Parameter')
        plt.ylabel('Time in ms')
        plt.title("Benchmark "+name)
        lgd = plt.legend(loc='center right', bbox_to_anchor=(1.4, 0.5))
        plt.savefig('../images/%s.png' % name, dpi=1000, bbox_extra_artists=(lgd,), bbox_inches='tight')
        plt.clf()

if __name__ == '__main__':
    generate_images()

import sys 
from .classmodule import MyClass
from .funcmodule import my_function
from .spotifymodule import getTrack
from .weathermodule import getCurrentWeather

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
        getTrack(arg)

   

if __name__ == '__main__':
    main()
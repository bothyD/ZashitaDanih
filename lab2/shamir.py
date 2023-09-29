import sys
print(sys.path)
sys.path.append('C:\python\ZashitaDanih\lab1')
from lab1.main import fastMulty

def main():
    print(fastMulty(5,20,7))

if __name__ =="__main__":
    main()
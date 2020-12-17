import re

def prompt_user():
    print("""
    **         Welcome MadLib Player!        **
    **       Get ready to have some fun      **
    **         Type during the prompt        **
           """)

def read_template(a):
    with open(a)as text:
        readtemp = text.read()
        return readtemp
# input file path  output returns file path

def parse_template(string):
    """ takes in string, return string with language parts removed, separate list with language parts 
    """ 
    parsed = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", string)) 
    # separate list with language parts

    length = len(parsed)
    for i in range(0,length):
        if( i == 0 ):
            print(i)
            parsed_string = string.replace(parsed[i],"")
        else:
            parsed_string = parsed_string.replace(parsed[i],'')
    return  parsed_string,parsed

def main():
    prompt_user()
    # parse_template()
    # read_template()

if __name__ == "__main__":
    # execute only if run as a script
    main()  

# def merge():
    


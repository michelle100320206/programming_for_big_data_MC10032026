import csv
import operator

changes_file = 'changes_python.txt'
def read_file(changes_file):
    # use strip to strip out spaces 
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # divide each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at deleted.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_authors(data):
    sep = 72*'-'
    authors = {}
    index = 0
    while index < len(data):
        try:
            # divide each of the authors and put them into a list of commits
            author = data[index + 1].split('|')[1].strip()
            if author in authors:
                authors[author] = authors[author] + 1
            else:
                authors[author] = 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors

#sorting the author list 
def sort_authors(authors):
    return sorted(authors.items(), key=operator.itemgetter(1))



if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    
    # print(len(data))
    #print(commits)
    # print(commits[0])
    # print(commits[1]['author'])
    # print(len(commits))
 

#printing to csv (assistance from stackoverflow)   
    keys = commits[0].keys()
    with open ('v4Michelle_10032026_writetocsv.csv', 'wb') as output_file: 
        dict_writer = csv.DictWriter (output_file, keys)
        dict_writer.writeheader ()
        dict_writer.writerows (commits)
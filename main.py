# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
# Create an empty dictionary
    counts = dict()
    words = filename.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def count_words():
    text = read_file_content("./story.txt")
# Open the file in read mode
file = open("story.txt", "r")

#read content of file to string
data = file.read()

# Print the number of occurrences of words in the text file
print( read_file_content(data))
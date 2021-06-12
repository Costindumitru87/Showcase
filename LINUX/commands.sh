# Display the current directory file path
pwd


# Change directory to /test directory
cd /test 


# Move up one level in the directory tree structure
cd ..  


# List files - both regular &  hidden files and their permissions as well
ls -al


# Creates a new file
touch file_name


# Copy files
cp original.txt duplicate.txt


# Move a file
mv autumn.csv winter.csv ..


# view a file's contents
cat agarwal.txt


# Rename files
mv course.txt old-course.txt


# Delete files
rm thesis.txt backup/thesis-2017-08.txt


# Look at the start of a file
head seasonal/summer.csv
head -n 3 seasonal/summer.csv


# List everything below a directory
ls -R


# Select columns from a file
cut -f 2-5,8 -d , values.csv


#S elect lines containing specific values
grep 2017-07 seasonal/spring.csv       

#grep's more common flags:
#-c: print a count of matching lines rather than the lines themselves
#-h: do not print the names of files when searching multiple files
#-i: ignore case (e.g., treat "Regression" and "regression" as matches)
#-l: print the names of files that contain matches, not the matches
#-n: print line numbers for matching lines
#-v: invert the match, i.e., only show lines that don't match



# Store a command's output in a file
head -n 5 seasonal/summer.csv > top.csv


# Use a command's output as an input
head -n 5 seasonal/winter.csv > top.csv
tail -n 3 top.csv


# How can I count the records in a file?
grep 2017-07 seasonal/spring.csv | wc -l


# Specify many files at once
cut -d , -f 1 seasonal/*


# Sort lines of text
cut -d, -f 2 seasonal/winter.csv | grep -v Tooth | sort -r


# Remove duplicate lines
cut -d, -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c


# Repeat a command many times
for filetype in gif jpg png; do echo $filetype; done


# Repeat a command once for each file
for filename in seasonal/*.csv; do echo $filename; done


# Run many commands in a single loop
for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done

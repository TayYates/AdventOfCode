Disclaimer: I am a Python developer who had zero experience with Golang or Rust going into this. I'm learning as I go; but if you're copying my work, just know that my Go/Rust are not going to be optimal and I probably write them with a Python accent.

Most of these were solved first in Python, then in Go, and finally in Rust

***
Day 1: parse text to integers, sort list, print max
  - Python's list comprehensions and built in max() and sorted() methods made this one a cakewalk.
  - Golang's bufio took an embarassingly long time for me to understand. It seems to be built with concurrency in mind, which I'm not taking advantage of here. Static typing was an irritant, but I was able to figure it out with a bit of googling
  - Rust has a very low level way of assigning datatypes. It seems very useful for embedded work, but those features weren't helpful for my use case. I did appreciate having the built in sort() and reverse() functions, and was pleasantly surprised by the readability

  - Overall, I was amazed by how efficiently the compiled Go and Rust were able to fire up and run when given a warm start; in this case 5x faster than the python interpreter
***
Day 2: for loop over a list, accessing dictionary values
- Honestly, this one was simple enough that I didn't notice any meaningful differences between writing the 3. Python called it a dictionary, Golang called it a map of strings/ints, and Rust called it a HashMap, but they all worked in the same way. I'm still impressed with the performance of Go and Rust, given that the syntax for each was so similar and the Python runtime was so much slower
***
Day 3: string manipulation, for loops, char -> ascii translation
- Simple vanilla Python, being able to easily split a string in half was very handy, and ASCII values made the prompt much easier to handle
- Golang felt needlessly verbose on this one, especially the for loops, but I still appreciated being able to split strings and use ASCII in a way that felt natural
- As frustrating as Rust's static typing was, the compiler is incredible, and usually had very good suggestions to fix my simple mistakes. Sometimes I was guessing with datatypes, but as long as it compiled and ran, I was happy

- Overall, I'm still impressed with the runtimes for Golang/Rust, but irritated with my own lack of experience with them
***
Day 4: regex and if/and/or logic
- In Python I skipped the regex by splitting the strings by '-', but it created an ugly situation where I had to convert everything to an int while using it. Definitely not optimal, I would rewrite this with regex and a separate section of casting the results as integers if it were going into production
- Golang and Rust were extremely similar here. Using regex and converting everything to integers meant that I could write very clean logic statements that were easy to walk through. This was helpful because the logic was the part that required brainpower
- I stopped compiling rust with rustc and instead started using cargo. This was necessary because of the regex, but I'm glad that I moved over
***
Day 5: parsing text into stacks, vector manipulation
- Python's list comprehensions and list-of-lists functionality made this very easy. The only pain point here was building the initial state of the crates. I did it in a very non-pythonic way and brute forced it to work. Also, there was a technical issue with how Python stores list items in memory; because it was a list-of-lists, I had to use deepcopy to keep them separate, otherwise the two parts would overwrite one another in memory
- Golang was a pain for this one. Datatype errors, difficulty appending to the front of an array, difficulty dealing with an array of arrays, etc. This one was irritating, but very satisfying once I finally got it
- I have the same complaints about Rust that I just mentioned with Go, but because I wrote this after the Go, I had already worked out most of those kinks. My big complaint here is how difficult it is to modify a vector of vectors. It was very frustrating to know that there was a reverse() function that did not work with my data type. In order to make it work, I would've had to completely rewrite how I had parsed the input data. So instead, I used tmp variables to store that data and then appended my stacks to that tmp variable

- I'm sure that there are much better ways to solve this in both Go and Rust, but I had a lot of difficulty with the static typing and not being able to intuitively use built-in functions because they were datatype specific. Getting better with them, but I'm definitely still suffering from a lack of experience
***
Day 6: read a string one character at a time, identifying unique sets
- Python feels like cheating on something like this. Sets are built in, easy to use, and automatically find the uniques
- The Go solution was easy after I figured out how to use a map to simulate Python sets. Having to make my own function to emulate this was easy enough, but I wish I could get the 'unique' package to work instead
- Rust was surprisingly inefficient in this task. I think it has something to do with having to rebuild new HashSets for every iteration; either that or the nested for loops because I couldn't index the string. Still faster than Python though
***
Day 7: directory walk simulator, storing cumulative values
- Vanilla Python to the rescue. No packages needed, just 1 list, 1 dict, and a few for loops
- Golang made this easy enough. I still had access to a lot of similar tools that i'm used to, albeit with some extra verbosity to account for the static typing
- Rust did not feel great to use for this problem. I still find it frustrating when the functions that intuitively should work, for some reason do not work for my particular data types. Trying to manipulate vectors in Rust feels like an invocation of Murphy's Law

- I decided to skip Rust on this one out of frustration, but hopefully I'll come back after I've learned more about the language
***
Day 8: modified local peaks problem
- I fought Python's numpy for a while trying to do this in a brute force way, but finally ended up solving it like a rubix cube; one side at a time, flipping it 90 degrees each time. Having access to numpy makes something like this approachable, when otherwise it would be daunting
***
Day 9: simulate a rope
- Python made this simple enough. The nested for loops were painful to write, but they work and < 1 second is good enough for a game. Might come back later and see if I can do some matrix math to speed it up
***
Day 10: simulate reading simple machine code and refreshing a screen
- Vanilla Python continues to make these approachable and enjoyable
Disclaimer: I am a Python developer who had zero experience with Golang or Rust going into this. I'm learning as I go; but if you're copying my work, just know that my Go/Rust are not going to be optimal and I probably write them with a Python accent.
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
Day 3: 

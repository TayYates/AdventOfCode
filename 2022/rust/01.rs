use std::{env, fs};

fn main() {
    let myString = fs::read_to_string("../data/01-1.txt".to_string()).unwrap();
    // println!("{}", myString);

    let mut sums: Vec<i32> = Vec::new();
    let mut current = 0;

    for line in myString.lines() {
        if line.is_empty() {
            sums.push(current);
            current = 0;
        } else {
            current += line.parse::<i32>().unwrap();
        }
    }
    sums.sort();
    sums.reverse();

    // part 1 answer
    println!("{}", sums[0]);

    // part 2 answer
    println!("{}", sums[0] + sums[1] + sums[2]);
}
use std::fs;
use std::collections::HashMap;

fn main() {
    let myString = fs::read_to_string("../data/02-1.txt".to_string()).unwrap();
    // println!("{}", myString);

    let scoreHash1 = HashMap::from([
        ("A X", 4),
        ("A Y", 8),
        ("A Z", 3),
        ("B X", 1),
        ("B Y", 5),
        ("B Z", 9),
        ("C X", 7),
        ("C Y", 2),
        ("C Z", 6),
    ]);
    let scoreHash2 = HashMap::from([
        ("A X", 3),
        ("A Y", 4),
        ("A Z", 8),
        ("B X", 1),
        ("B Y", 5),
        ("B Z", 9),
        ("C X", 2),
        ("C Y", 6),
        ("C Z", 7),
    ]);

    let mut score1 = 0;
    let mut score2 = 0;

    for line in myString.lines() {
        score1 += scoreHash1[&line];
        score2 += scoreHash2[&line];
    }
    // part 1 answer
    println!("{}", score1);
    // part 2 answer
    println!("{}", score2);
}
use std::fs;
use regex::Regex;

fn main() {
    let my_string = fs::read_to_string("../../../../data/04-1.txt".to_string()).unwrap();
    //println!("{}", my_string);

    let re = Regex::new(r"(\d+)-(\d+),(\d+)-(\d+)").unwrap();
    let mut score1 = 0;
    let mut score2 = 0;

    for line in my_string.lines() {
        let caps = re.captures(line).unwrap();
        let a = caps.get(1).unwrap().as_str().parse::<i32>().unwrap();
        let b = caps.get(2).unwrap().as_str().parse::<i32>().unwrap();
        let c = caps.get(3).unwrap().as_str().parse::<i32>().unwrap();
        let d = caps.get(4).unwrap().as_str().parse::<i32>().unwrap();
        //println!("a: {}, b: {}, c: {}, d: {}", a, b, c, d);

        if (a <= c && b >= d) || (c <= a && d >= b) {
            score1 += 1;
        }
        if (a <= d && b >= c) || (c <= a && d >= b) {
            score2 += 1;
        }
    }
    // part 1 answer
    println!("{}", score1);
    // part 2 answer
    println!("{}", score2);
}

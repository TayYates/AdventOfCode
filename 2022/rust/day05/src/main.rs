use std::fs;
use regex::Regex;

fn main() {
    let moves_string = fs::read_to_string("../../data/05-moves.txt".to_string()).unwrap();
    let crates_string = fs::read_to_string("../../data/05-crates.txt".to_string()).unwrap();

    // build moves
    let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap();
    let mut moves: Vec<(usize, usize, usize)> = Vec::new();
    for line in moves_string.lines() {
        let caps = re.captures(line).unwrap();
        let count = caps.get(1).unwrap().as_str().parse::<usize>().unwrap();
        let mut from = caps.get(2).unwrap().as_str().parse::<usize>().unwrap();
        from -= 1;
        let mut to = caps.get(3).unwrap().as_str().parse::<usize>().unwrap();
        to -= 1;
        moves.push((count, from, to));
    }
    //println!("{:?}", moves);

    // build initial stacks
    let mut stacks: Vec<Vec<char>> = Vec::new();
    for _ in 0..9 {
        stacks.push(Vec::new());
    }
    for line in crates_string.lines() {
        for (i, c) in line.chars().enumerate() {
            if c != ' ' && c!= '[' && c!= ']' {
                stacks[i/4].push(c);
            }
        }
    }
    // initial state
    stacks.iter()
      .for_each(|s| print!("{:?}", s.first().unwrap()));
      println!();

    let mut stacks2: Vec<Vec<char>> = stacks.clone();

    for (count, from, to) in moves {
        for i in 0..count {
            // part 1 work
            let mut x: Vec<char> = [stacks[from][0]].to_vec();
            x.append(&mut stacks[to]);
            stacks[to] = x;
            stacks[from].remove(0);

            // part 2 work
            let mut y: Vec<char> = [stacks2[from][count-i-1]].to_vec();
            y.append(&mut stacks2[to]);
            stacks2[to] = y;
            stacks2[from].remove(count-i-1);
        }
    }
    // part 1 answer
    stacks.iter()
      .for_each(|s| print!("{:?}", s.first().unwrap()));
    println!();

    // part 2 answer
    stacks2.iter()
      .for_each(|s| print!("{:?}", s.first().unwrap()));

}


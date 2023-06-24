use std::fs;

fn ascii_score(c: char) -> u32 {
  let ascii = c as u32;
  if ascii >= 97 {
    return ascii - 96;
  } else {
    return ascii - 38;
  }
}

fn find_double(s1: &str, s2: &str) -> char {
  for c in s1.chars() {
    if s2.contains(c) {
      return c;
    }
  }
  return ' ';
}

fn find_triple(s1: &str, s2: &str, s3: &str) -> char {
  for c in s1.chars() {
    if s2.contains(c) && s3.contains(c) {
      return c;
    }
  }
  return ' ';
}

fn main() {
  let my_string = fs::read_to_string("../data/03-1.txt".to_string()).unwrap();
  // println!("{}", myString);

  let mut score = 0;
  for line in my_string.lines() {
    //println!("{}", find_double("abcd", "defg"));
    let halves = line.split_at(line.len() / 2);
    let double = find_double(halves.0, halves.1);
    score += ascii_score(double);
  }

  // part 1 answer
  println!("{}", score);
  
  score = 0;
  let mut lines = my_string.lines();
  while let (Some(line1), Some(line2), Some(line3)) = (lines.next(), lines.next(), lines.next()) {
    let triple = find_triple(line1, line2, line3);
    score += ascii_score(triple);
  }
  
  // part 2 answer
  println!("{}", score);
}
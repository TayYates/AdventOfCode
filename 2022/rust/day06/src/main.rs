use std::fs;
use std::collections::HashSet;

fn main() {
  let input = fs::read_to_string("../../data/06-1.txt").unwrap();
  //println!("{}", input);

  let input_bytes = input.as_bytes();
  let mut ans1 = 0;
  let mut ans2 = 0;

  for i in 0..input.len() {
    //println!("{}", input_bytes[i]);
    let mut set1: HashSet<usize> = HashSet::new();
    for j in i..i+4 {
      set1.insert(input_bytes[j] as usize);
    }
    let mut set2: HashSet<usize> = HashSet::new();
    for k in i..i+14 {
      set2.insert(input_bytes[k] as usize);
    }
    if set1.len() == 4 && ans1 == 0{
      ans1 = i+4;
      // part 1 answer
      println!("{}", ans1);
    }
    if set2.len() == 14 && ans2 == 0{
      ans2 = i+14;
      // part 2 answer
      println!("{}", ans2);
      break;
    }
  }
}

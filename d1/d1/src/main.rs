use rayon::prelude::*;
use std::fs::read_to_string;

fn main() {
    let sum: u32 = read_to_string("input").unwrap().lines().par_bridge().map(|s|->u32{

        let first_digit = s.chars().find(|&x| x>= '0' && x<= '9').unwrap();
        let last_digts = s.chars().rev().find(|&x| x>= '0' && x<= '9').unwrap();

        first_digit.to_digit(10).unwrap() * 10 + last_digts.to_digit(10).unwrap()
    }).sum();

    println!("{:?}", sum);
}

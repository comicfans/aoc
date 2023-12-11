use rayon::prelude::*;
use regex::Regex;
use std::fs::read_to_string;

fn main() {
    //Game 1: 1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green


    let sum: u32 = read_to_string("input").unwrap().lines().par_bridge().map(|s|->u32{

        let number_str= s.split(":").nth(0).unwrap().split(" ").nth(1).unwrap();

        let game_number = number_str.parse::<u32>().unwrap();

        for str in s.split(":").nth(1).unwrap().split(";"){

            for number_color in str.split(","){
                let number_str  = number_color.strip_prefix(" ").unwrap().split(" ").nth(0);
                let number = number_str.unwrap().parse::<i32>().unwrap();
                let color = number_color.strip_prefix(" ").unwrap().split(" ").nth(1).unwrap();

                //only 12 red cubes, 13 green cubes, and 14 blue 
                let max = match color{
                    "red"=>{
                        12
                    },
                    "blue"=>{
                        14
                    },
"green"=>{
                        13
                    }
                    _=>{
                        panic!();
                    }
                };

                if number > max{
                    return 0;
                }
            }
        }
        
        return game_number;
         
    }).sum();


    println!("{:?}", sum);
}

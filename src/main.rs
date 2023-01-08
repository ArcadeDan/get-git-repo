
use std::env;

fn main() {
    //println!("Hello, world!");

    let args: Vec<String> = env::args().collect();

    let file = std::fs::read(args[1].to_string() + &".txt".to_string());

    dbg!(file);
}

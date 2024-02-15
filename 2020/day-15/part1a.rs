use std::fs::read_to_string;
use std::time::Instant;

const FILEPATH: &str = "../../_inputs/2020/day-15/input.txt";

fn main() {
    let now = Instant::now();

    let maxl = 30_000_000;

    let input: Vec<_> = read_to_string(FILEPATH)
        .unwrap()
        .lines()
        .map(|x| x.trim())
        .map(String::from)
        .collect();

    let input: Vec<u64> = input[0]
        .split(",")
        .map(|n| n.parse::<u64>().unwrap())
        .collect::<Vec<u64>>();

    let mut count = Vec::<u64>::new();
    count.resize(maxl, 0 as u64);

    for (i, &num) in input.iter().enumerate() {
        count[num as usize] = (i + 1) as u64;
    }

    let mut prev: u64 = input[input.len() - 1];

    for i in 7..=maxl {
        if i == 2021 {
            println!("Part 1: {prev}");
        }

        let nxt: u64 = if count[prev as usize] != 0 {
            ((i - 1) as u64) - count[prev as usize]
        } else {
            0
        };

        count[prev as usize] = (i - 1) as u64;
        prev = nxt;
    }
    println!("Part 2: {prev}");

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}

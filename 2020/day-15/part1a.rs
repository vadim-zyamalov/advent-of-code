use std::time::Instant;

fn main() {
    let now = Instant::now();
    let input: [u64; 6] = "18,11,9,0,5,1".split(",")
                                         .map(|n| n.parse::<u64>().unwrap())
                                         .collect::<Vec<u64>>()
                                         .try_into()
                                         .unwrap();
    let maxl = 30_000_000;
    let mut count = Vec::<u64>::new();
    count.resize(maxl, 0 as u64);

    for (i, num) in input.iter().enumerate() {
        count[*num as usize] = (i + 1) as u64;
    }

    let mut prev: u64 = input[input.len() - 1];

    for i in 7..=30_000_000 {
        if i == 2021 {
            println!("Part 1: {prev}");
        }

        let nxt = if count[prev as usize] != 0 {
            (i - 1) - count[prev as usize]
        } else {
            0
        };

        count[prev as usize] = i - 1;
        prev = nxt;
    }
    println!("Part 2: {prev}");

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}
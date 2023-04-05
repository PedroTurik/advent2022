use itertools::Itertools;
use std::collections::{HashMap, HashSet};

mod helper;

fn dive<'a>(
    cur: &'a String,
    mut visited: HashSet<&'a String>,
    min_left: i32,
    saved: i32,
    to_go: &Vec<String>,
    distances: &HashMap<String, HashMap<String, i32>>,
    flows: &HashMap<String, i32>,
) -> i32 {
    if visited.len() == to_go.len() + 1 || min_left <= 0 {
        return saved;
    }

    visited.insert(&cur);
    let mut maximum = 0;
    for dest in to_go {
        if !visited.contains(&dest) {
            let cur_min = min_left - (distances.get(cur).unwrap().get(dest).unwrap() + 1);
            let cur_save = saved
                + (if cur_min >= 0 {
                    cur_min * flows.get(dest).unwrap()
                } else {
                    0
                });
            let ans = dive(
                dest,
                visited.clone(),
                cur_min,
                cur_save,
                to_go,
                distances,
                flows,
            );
            if ans > maximum {
                maximum = ans;
            }
        }
    }
    maximum
}

fn part1() {
    let (to_go, distances, flows) = helper::structures("./input.txt");

    let to_go: Vec<String> = to_go.iter().map(|x| x.to_owned()).collect();
    println!(
        "part1: {}",
        dive(
            &"AA".to_owned(),
            HashSet::new(),
            30,
            0,
            &to_go,
            &distances,
            &flows
        )
    )
}

fn part2() {
    let (to_go, distances, flows) = helper::structures("./input.txt");

    let to_go: Vec<String> = to_go.iter().map(|x| x.to_owned()).collect();

    let mut maior = 0;

    for set in to_go.iter().map(|x| x.to_owned()).combinations(7) {
        let elef_vec: Vec<String> = to_go
            .clone()
            .iter()
            .filter(|x| !set.contains(x))
            .map(|x| x.to_owned())
            .collect();
        let aux = 
            dive(
            &"AA".to_owned(),
            HashSet::new(),
            26,
            0,
            &set,
            &distances,
            &flows,
        )
        +
            dive(
            &"AA".to_owned(),
            HashSet::new(),
            26,
            0,
            &elef_vec,
            &distances,
            &flows,
        );

        if aux > maior {
            maior = aux;
        }
    }

    println!("part2: {}", maior);
}

fn main() {
    part1();
    part2();
}

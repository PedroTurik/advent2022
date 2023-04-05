use itertools::Itertools;
use std::{collections::{HashMap, HashSet}, thread, sync::{Arc, Mutex}};

mod helper;

fn dive<'a>(
    cur: &'a String,
    mut visited: HashSet<&'a String>,
    min_left: i32,
    saved: i32,
    to_go: &Vec<String>,
    distances: Arc<Mutex<HashMap<String, HashMap<String, i32>>>>,
    flows: Arc<Mutex<HashMap<String, i32>>>,
) -> i32 {
    if visited.len() == to_go.len() + 1 || min_left <= 0 {
        return saved;
    }

    visited.insert(&cur);
    let mut maximum = 0;
    for dest in to_go {
        if !visited.contains(&dest) {
            let cur_min = min_left - (distances.lock().unwrap().get(cur).unwrap().get(dest).unwrap() + 1);
            let cur_save = saved
                + (if cur_min >= 0 {
                    cur_min * flows.lock().unwrap().get(dest).unwrap()
                } else {
                    0
                });
            let ans = dive(
                dest,
                visited.clone(),
                cur_min,
                cur_save,
                to_go,
                Arc::clone(&distances),
                Arc::clone(&flows),
            );
            if ans > maximum {
                maximum = ans;
            }
        }
    }
    maximum
}


fn part2() {
    let (to_go, distances, flows) = helper::structures("./input.txt");

    let to_go: Vec<String> = to_go.iter().map(|x| x.to_owned()).collect();

    let mut maior = 0;

    let flows = Arc::new(Mutex::new(flows));
    let distances = Arc::new(Mutex::new(distances));
    for set in to_go.iter().map(|x| x.to_owned()).combinations(7) {
        let elef_vec: Vec<String> = to_go.clone().iter().filter(|x| !set.contains(x)).map(|x| x.to_owned()).collect();
        let man_dist = Arc::clone(&distances);
        let man_flow = Arc::clone(&flows);
        let elef_dist = Arc::clone(&distances);
        let elef_flow = Arc::clone(&flows);

        let handle1 = thread::spawn(move || -> i32 {
            dive(&"AA".to_owned(), HashSet::new(), 26, 0, &set, man_dist, man_flow)
        });

        let handle2 = thread::spawn(move || -> i32 {
            dive( &"AA".to_owned(), HashSet::new(), 26, 0, &elef_vec, elef_dist, elef_flow)
        });

        let result = handle1.join().unwrap() + handle2.join().unwrap();
        if  result > maior {
            maior = result;
        }
    }

    println!("part2: {}", maior);
}

fn main() {
    part2();
}

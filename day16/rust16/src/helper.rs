use std::collections::{HashMap, HashSet, VecDeque};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;



fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn structures(path: &str) -> (HashSet<String>, HashMap<String, HashMap<String, i32>>, HashMap<String, i32>){
    let mut tunnels:HashMap<String, Vec<String>> = HashMap::new();
    let mut flows:HashMap<String, i32> = HashMap::new();
    let mut to_go: HashSet<String> = HashSet::new();
    let mut distances:HashMap<String, HashMap<String, i32>> = HashMap::new();

    if let Ok(lines) = read_lines(path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(data) = line {
                let info: Vec<String>= data.split(' ').map(|x| { x.to_owned()}).collect();
                let flow = info[4][5..info[4].len()-1].parse::<i32>().unwrap();
                let start = info[1].to_owned();

                let mut tmp_vec: Vec<String> = vec![]; 

                for dest in &info[9..]{
                    tmp_vec.push(dest[..2].to_owned())
                }

                tunnels.insert(start.clone(), tmp_vec);

                if flow != 0{
                    flows.insert(start.clone(), flow);
                    to_go.insert(start.clone());
                }
            }
        }
    }

    for (start, _dests) in tunnels.clone(){
        if !to_go.contains(&start) && start != "AA".to_owned(){ continue;}

        let mut visited: HashSet<String> = HashSet::new();
        visited.insert(start.clone());
        let mut dic_tmp: HashMap<String, i32> = HashMap::new();
        let mut queue = VecDeque::from([(start.clone(), 0)]);
        while !queue.is_empty() {
            if dic_tmp.len() == (if !to_go.contains(&start) {to_go.len()} else {to_go.len()-1}){
                distances.insert(start, dic_tmp);
                break;
            }

            let (source, dist) = queue.pop_front().unwrap();


            for x in tunnels.get(&source).unwrap(){
                if !visited.contains(x){
                    if to_go.contains(x){
                        dic_tmp.insert(x.to_string(), dist+1);
                    }
                    queue.push_back((x.to_string(), dist+1));
                    visited.insert(x.to_string());

                }
            }

        }

    }

    (to_go, distances, flows)

}


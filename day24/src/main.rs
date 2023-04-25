use std::{io, collections::{HashSet, VecDeque}, env};

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Direction {
    Right,
    Left,
    Up,
    Down,
    Dead,
}

#[derive(Debug)]
struct Blizzard {
    y: usize,
    x: usize,
    direction: Direction,
}

impl Blizzard {
    fn wind(&mut self){
        match self.direction {
            Direction::Down => self.y = (self.y + 1)%35,
            Direction::Left => self.x = if self.x == 0 {99} else {self.x-1},
            Direction::Right => self.x = (self.x+1)%100,
            Direction::Up => self.y = if self.y == 0 {34} else {self.y-1},
            Direction::Dead => {}
            
        }
    }
}





fn get_matrixes() -> [[[bool; 100]; 35]; 700] {
    let mut start_matrix: Vec<Blizzard> = Vec::new();

    for (i, s) in io::stdin().lines().enumerate() {
        if i == 0 || i == 36 {
            continue;
        }
        for (j, c) in s.unwrap().chars().enumerate() {
            if j == 0 || j == 101 {
                continue;
            }
            start_matrix.push(Blizzard {
                y: i - 1,
                x: j - 1,
                direction: match c {
                    'v' => Direction::Down,
                    '^' => Direction::Up,
                    '>' => Direction::Right,
                    '<' => Direction::Left,
                    '.' => Direction::Dead,
                    _ => panic!("veio coisa sus no input")           
                },
            });
        }
    }

    let mut ret_matrixes: [[[bool; 100]; 35]; 700] = [[[false; 100]; 35]; 700];

    for k in 0..700{
        for b in start_matrix.iter_mut(){
            if b.direction != Direction::Dead{
                ret_matrixes[k][b.y][b.x] = true;
                b.wind();
            }
        }
    }


    return ret_matrixes;
}

#[derive(Debug, Clone, Hash, PartialEq, Eq, Copy)]
struct Player {
    y: usize,
    x: usize,
    minutes: usize
}

impl Player {
    fn move_left(&self) -> Player{
        Player { y: self.y, x: self.x - 1, minutes: self.minutes + 1 }
    }
    fn move_right(&self) -> Player{
        Player { y: self.y, x: self.x + 1, minutes: self.minutes + 1 }
    }
    fn move_up(&self) -> Player{
        Player { y: self.y - 1, x: self.x, minutes: self.minutes + 1 }
    }
    fn move_down(&self) -> Player{
        Player { y: self.y + 1, x: self.x, minutes: self.minutes + 1 }
    }

    fn wait(&self) -> Player{
        Player { y: self.y, x: self.x, minutes: self.minutes + 1 }
    }

    fn check_finish(&self, y: usize, x: usize) -> bool{
        self.y == y && self.x == x 
    }



}



fn part1() {
    let matrixes = get_matrixes();
    let mut queue: VecDeque<Player> = VecDeque::new();
    let mut seen: HashSet<Player> = HashSet::new();
    queue.push_back(Player { y: 100, x: 0, minutes: 0 });

    while !queue.is_empty() {
        let cur_player = queue.pop_front().unwrap();
        if cur_player.check_finish(34, 99){
            println!("Parte 1: {:?}", cur_player);
            break;
        }
        let cur_frame = matrixes[cur_player.minutes%700];
        
        if cur_player.y == 100{
            if !cur_frame[0][0]{
                queue.push_back(Player { y: 0, x: 0, minutes: cur_player.minutes + 1 })
            }else {    
                queue.push_back(cur_player.wait());
            }

            continue;
        }

        if cur_player.x < 99 && !cur_frame[cur_player.y][cur_player.x+1]{
            let aux = cur_player.move_right();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.y < 34 && !cur_frame[cur_player.y+1][cur_player.x]{
            let aux = cur_player.move_down();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.x > 0 && !cur_frame[cur_player.y][cur_player.x-1]{
            let aux = cur_player.move_left();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.y > 0 && !cur_frame[cur_player.y-1][cur_player.x]{
            let aux = cur_player.move_up();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if !cur_frame[cur_player.y][cur_player.x]{
            let aux = cur_player.wait();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }

    }

}


fn part2(){
    let matrixes = get_matrixes();
    let mut queue: VecDeque<Player> = VecDeque::new();
    let mut seen: HashSet<Player> = HashSet::new();
    queue.push_back(Player { y: 100, x: 0, minutes: 0 });
    
    let mut y_goal: usize = 34; 
    let mut x_goal: usize = 99;
    let mut counter = 0;
    while !queue.is_empty() {
        let cur_player = queue.pop_front().unwrap();
        if cur_player.check_finish(y_goal, x_goal){
            println!("{:?}", cur_player);
            counter += 1;
            if counter == 3 {
                println!("porraaa {:?}", cur_player);
                break;
            }
            queue.clear();
            seen.clear();
            
            if y_goal == 0{
                y_goal = 34;
                x_goal = 99;
                queue.push_back(Player { y: 100, x: 0, minutes: cur_player.minutes });

            }else{
                y_goal = 0;
                x_goal = 0;
                queue.push_back(Player { y: 200, x: 99, minutes: cur_player.minutes });
            }
            

        }
        let cur_frame = matrixes[cur_player.minutes%700];
        
        if cur_player.y == 200 {
            if !cur_frame[34][99]{
                queue.push_back(Player { y: 34, x: 99, minutes: cur_player.minutes + 1 })
            }else {    
                queue.push_back(cur_player.wait());
            }

            continue;
        }


        if cur_player.y == 100{
            if !cur_frame[0][0]{
                queue.push_back(Player { y: 0, x: 0, minutes: cur_player.minutes + 1 })
            }else {    
                queue.push_back(cur_player.wait());
            }

            continue;
        }

        if cur_player.x < 99 && !cur_frame[cur_player.y][cur_player.x+1]{
            let aux = cur_player.move_right();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.y < 34 && !cur_frame[cur_player.y+1][cur_player.x]{
            let aux = cur_player.move_down();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.x > 0 && !cur_frame[cur_player.y][cur_player.x-1]{
            let aux = cur_player.move_left();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if cur_player.y > 0 && !cur_frame[cur_player.y-1][cur_player.x]{
            let aux = cur_player.move_up();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }
        if !cur_frame[cur_player.y][cur_player.x]{
            let aux = cur_player.wait();
            if !seen.contains(&aux){
                seen.insert(aux);
                queue.push_back(aux);
            }
        }

    }

}

fn main() {
    
    let a: Vec<String> = env::args().collect();

    let a = a.get(1).unwrap();
    match a.as_str() {
        "1" => {
            part1()
        },
        "2" => {
            part2()
        },
        _ => println!("Write 1 or 2")
    };
}

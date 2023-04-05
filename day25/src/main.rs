use std::io::stdin;


fn vec_to_snafu(v: Vec<i64>) -> String{
    let mut ret = "".to_owned();
    for n in v.iter().rev(){
        ret.push_str(
            match n {
                -2 => "=",
                -1 => "-",
                 0 => "0",
                 1 => "1",
                 2 => "2",
                _ => panic!(),
                
            }
        )
    }

    return ret;
}


fn closest_5_pow(mut num: i64) -> u32{
    num = num.abs();
    let lg = ((num as f64).ln() / (5 as f64).ln()) as u32;

    let a = 5_i64.pow(lg);
    let b = 5_i64.pow(lg+1);
    if num - a > b - num{
        return lg+1;
    }

    return lg;


    
}

fn i64_to_snafu(mut num: i64) -> Vec<i64>{
    let mut v: Vec<i64> = vec![0;30];
    loop {
        if num == 0 {break;}

        let x = closest_5_pow(num);
        let constant = 5_i64.pow(x);
    
        let mut closer: (u64, i64) = (num as u64, 0);
    
        for i in -2_i64..3{
            let aux = constant*i;
            if aux.abs_diff(num) < closer.0{
                closer.0 = aux.abs_diff(num);
                closer.1 = i
            }
        }

        num -= closer.1*constant;

        if v[x as usize] != 0{
            println!("fuck");
            break;
        }

        v[x as usize] = closer.1
    }

    return v;
}

fn snafu_to_i64(sn: String) -> i64{
    let mut total = 0;
    let base: i64 = 5;
    for (i, c) in sn.chars().rev().enumerate(){
        match c {
            '=' => total += base.pow(i as u32)*-2,
            '-' => total += base.pow(i as u32)*-1,
            '1' => total += base.pow(i as u32),
            '2' => total += base.pow(i as u32)*2,
            '0' => continue,
            _ => panic!("What the fuck")
        }
    }

    return total;
}

fn main() {
    let stdin = stdin();
    let snafus = stdin.lines();

    let mut total = 0;

    for num in snafus{
        total += snafu_to_i64(num.unwrap());
    }

    println!("{total}");

    let a = i64_to_snafu(total);
    println!("{:?}", a);
    println!("{}", vec_to_snafu(a));

    println!("{}", snafu_to_i64("2=-0=01----22-0-1-10".to_owned()));

}


// -120==202-0=--
fn ft_strlen(s: &str) -> usize {
    let mut i: usize = 0;
    for _ in  s.chars(){
        i += 1;
    }
    i
}

pub fn ft_split(s1: &str, c: char) -> Vec<&str> {
    let mut split: Vec<&str> = vec![];
    let mut j: usize = 0;
    let mut k: usize = 0;
    for (index, letter) in s1.chars().enumerate() {
        if letter == c {
            split.push(&s1[j..index]);
            j = index + 1;
        }
        k = index;
    }
    split.push(&s1[j..k + 1]);
    split
}

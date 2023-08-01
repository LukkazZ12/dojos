pub fn ft_strlen(s: &str) -> i32 {
    let mut i: i32 = 0;
    for _ in  s.chars(){
        i += 1;
    }
    i
}

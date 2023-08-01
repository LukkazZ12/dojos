mod ft_putstr;
mod ft_strlen;
mod ft_strcpy;
mod ft_strjoin;
mod ft_split;

use ft_putstr::ft_putstr;
use ft_strlen::ft_strlen;
use ft_strcpy::ft_strcpy;
use ft_strjoin::ft_strjoin;
use ft_split::ft_split;

fn main() {
    let dest: String = "".to_string();
    ft_putstr("Hello, Cadetes!".to_string());
    println!("tamanho {}", ft_strlen("Hello, Cadetes!"));
    println!("{}", ft_strcpy(dest, "Rust do caralho!"));
    println!("{}", ft_strjoin("Rust ".to_string(), "do capeta!"));
    println!("{:?}", ft_split("dale ideia", ' '));
}
